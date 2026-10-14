from flask import Flask, render_template, request, redirect, url_for, session, flash
from database import init_db, get_db_connection
from knowledge_base import SYMPTOMS, KNOWLEDGE_BASE
from inference_engine import run_forward_chaining, run_backward_chaining
import datetime

app = Flask(__name__)
app.secret_key = 'medibot_secret_key_123'

# Initialize database tables
init_db()

@app.route('/')
def home():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password)).fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['name']
            session['user_email'] = user['email']
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password', 'danger')
            
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
            conn.commit()
            conn.close()
            flash('Registration successful! Please login.', 'success')
            return redirect(url_for('login'))
        except:
            conn.close()
            flash('Email already registered!', 'danger')
            
    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    user_id = session['user_id']
    conn = get_db_connection()
    count_row = conn.execute('SELECT COUNT(*) as count FROM history WHERE user_id = ?', (user_id,)).fetchone()
    conn.close()
    
    total_assessments = count_row['count'] if count_row else 0
    total_symptoms = len(SYMPTOMS)
    total_rules = len(KNOWLEDGE_BASE)
    
    return render_template(
        'dashboard.html', 
        total_assessments=total_assessments, 
        total_symptoms=total_symptoms, 
        total_rules=total_rules
    )

@app.route('/assessment', methods=['GET', 'POST'])
def assessment():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    result = None
    selected = []
    
    if request.method == 'POST':
        selected = request.form.getlist('symptoms')
        result = run_forward_chaining(selected)
        
        # Save to database history
        user_id = session['user_id']
        symptoms_str = ", ".join(selected) if selected else "None"
        rules_str = ", ".join(result['matched_rules']) if result['matched_rules'] else "No Matches"
        diag_str = ", ".join(result['diagnoses']) if result['diagnoses'] else "Inconclusive"
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO history (user_id, symptoms, matched_rules, diagnosis, mode, created_at) VALUES (?, ?, ?, ?, ?, ?)',
            (user_id, symptoms_str, rules_str, diag_str, 'Forward Chaining', created_at)
        )
        conn.commit()
        conn.close()
        
    return render_template('assessment.html', symptoms=SYMPTOMS, result=result, selected=selected)

@app.route('/backward_check', methods=['GET', 'POST'])
def backward_check():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    result = None
    selected_symptoms = []
    target_disease = list(KNOWLEDGE_BASE.keys())[0]
    diseases = list(KNOWLEDGE_BASE.keys())
    
    if request.method == 'POST':
        target_disease = request.form.get('disease')
        selected_symptoms = request.form.getlist('symptoms')
        result = run_backward_chaining(target_disease, selected_symptoms)
        
        user_id = session['user_id']
        symptoms_str = ", ".join(selected_symptoms) if selected_symptoms else "None"
        rules_str = f"Goal: {target_disease}"
        diag_str = f"Verified ({result['match_pct']}%)" if result['is_verified'] else "Unverified (0%)"
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        conn = get_db_connection()
        conn.execute(
            'INSERT INTO history (user_id, symptoms, matched_rules, diagnosis, mode, created_at) VALUES (?, ?, ?, ?, ?, ?)',
            (user_id, symptoms_str, rules_str, diag_str, 'Backward Chaining', created_at)
        )
        conn.commit()
        conn.close()
        
    return render_template('backward_check.html', symptoms=SYMPTOMS, diseases=diseases, target_disease=target_disease, selected_symptoms=selected_symptoms, result=result)

@app.route('/history')
def history():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    user_id = session['user_id']
    conn = get_db_connection()
    logs = conn.execute('SELECT * FROM history WHERE user_id = ? ORDER BY id DESC', (user_id,)).fetchall()
    conn.close()
    
    return render_template('history.html', history=logs)

@app.route('/delete_history/<int:log_id>', methods=['POST'])
def delete_history(log_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    user_id = session['user_id']
    conn = get_db_connection()
    conn.execute('DELETE FROM history WHERE id = ? AND user_id = ?', (log_id, user_id))
    conn.commit()
    conn.close()
    return redirect(url_for('history'))

@app.route('/clear_all_history', methods=['POST'])
def clear_all_history():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    user_id = session['user_id']
    conn = get_db_connection()
    conn.execute('DELETE FROM history WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('history'))

@app.route('/how_it_works')
def how_it_works():
    return render_template('how_it_works.html' , knowledge_base=KNOWLEDGE_BASE)

if __name__ == '__main__':
    app.run(debug=True)