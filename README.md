# 🩺 MediBot: Clinical Diagnostic Intelligence Workstation

A custom rule-based medical expert system built with Python, Flask, and SQLite, featuring both **forward-chaining** inference for symptom-match likelihood ranking and **backward-chaining** for goal-driven hypothesis verification.

---

## 🌟 Live Demonstration
* **Live App URL:** [(https://medi-bot-sage.vercel.app/)](https://medi-bot-sage.vercel.app/)

---

## 🧠 System Architecture & Features
* **Knowledge Base (`knowledge_base.py`):** Encodes 102 medical symptoms and 18 rule-driven IF-THEN clinical conditions.
* **Inference Engine (`inference_engine.py`):** 
  * *Forward Inference:* Evaluates patient-reported symptoms against rule premises to rank possible conditions by match likelihood.
  * *Backward Inference:* Tests a target hypothesis goal by working backward through required logical rule conditions.
* **Secure Authentication & Workstation UI:** Modern glassmorphic split-screen interface built with Flask-Login, SQLite user profiles, and responsive dashboards displaying confidence progress bars, symptom match metrics, and medical precautions.

---

## 🛠️ Tech Stack
* **Backend:** Python, Flask, SQLite
* **Frontend:** HTML5, CSS3 (Glassmorphism design), JavaScript, FontAwesome
* **Deployment:** Vercel (Serverless Python Functions)
