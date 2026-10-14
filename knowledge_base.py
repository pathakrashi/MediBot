# Expanded Knowledge Base with 102 Symptoms for Comprehensive Forward & Backward Chaining

SYMPTOMS = [
    # Respiratory & ENT Symptoms (1-20)
    {"id": "fever", "name": "Fever", "desc": "Elevated body temperature above 100.4°F"},
    {"id": "cough", "name": "Cough", "desc": "Persistent dry or productive cough"},
    {"id": "sore_throat", "name": "Sore Throat", "desc": "Pain or irritation in the throat"},
    {"id": "sneezing", "name": "Sneezing", "desc": "Frequent involuntary sneezing"},
    {"id": "runny_nose", "name": "Runny Nose", "desc": "Excess nasal drainage or congestion"},
    {"id": "shortness_of_breath", "name": "Shortness of Breath", "desc": "Difficulty breathing or tightness"},
    {"id": "nasal_congestion", "name": "Nasal Congestion", "desc": "Blocked or stuffed nasal passages"},
    {"id": "wheezing", "name": "Wheezing", "desc": "High-pitched whistling sound during breathing"},
    {"id": "loss_of_smell", "name": "Loss of Smell", "desc": "Anosmia or diminished sense of smell"},
    {"id": "loss_of_taste", "name": "Loss of Taste", "desc": "Ageusia or diminished sense of taste"},
    {"id": "hoarseness", "name": "Hoarseness", "desc": "Raspy or strained voice"},
    {"id": "chest_tightness", "name": "Chest Tightness", "desc": "Sensation of pressure or constriction in chest"},
    {"id": "rapid_breathing", "name": "Rapid Breathing", "desc": "Tachypnea or abnormally fast breathing"},
    {"id": "stridor", "name": "Stridor", "desc": "Harsh, vibrating noise during breathing"},
    {"id": "sinus_pressure", "name": "Sinus Pressure", "desc": "Pain or pressure behind eyes and cheeks"},
    {"id": "earache", "name": "Earache", "desc": "Pain or throbbing in one or both ears"},
    {"id": "ear_fullness", "name": "Ear Fullness", "desc": "Sensation of fluid or pressure in ear"},
    {"id": "tinnitus", "name": "Tinnitus", "desc": "Ringing or buzzing in the ears"},
    {"id": "post_nasal_drip", "name": "Post-Nasal Drip", "desc": "Mucus dripping down the back of throat"},
    {"id": "bloody_nose", "name": "Bloody Nose", "desc": "Epistaxis or nasal bleeding"},

    # Pain & Neurological Symptoms (21-40)
    {"id": "headache", "name": "Headache", "desc": "Throbbing or continuous head pain"},
    {"id": "body_pain", "name": "Body Pain", "desc": "General muscle aches and weakness"},
    {"id": "joint_pain", "name": "Joint Pain", "desc": "Stiffness or ache in body joints"},
    {"id": "neck_stiffness", "name": "Neck Stiffness", "desc": "Difficulty turning or bending neck"},
    {"id": "dizziness", "name": "Dizziness", "desc": "Lightheadedness or feeling faint"},
    {"id": "sensitivity_to_light", "name": "Sensitivity to Light", "desc": "Photophobia or eye pain in bright light"},
    {"id": "sensitivity_to_sound", "name": "Sensitivity to Sound", "desc": "Phonophobia or discomfort from noise"},
    {"id": "confusion", "name": "Confusion", "desc": "Disorientation or difficulty thinking clearly"},
    {"id": "memory_loss", "name": "Memory Loss", "desc": "Short-term forgetfulness or brain fog"},
    {"id": "numbness", "name": "Numbness", "desc": "Loss of sensation in limbs or extremities"},
    {"id": "tingling", "name": "Tingling", "desc": "Pins and needles sensation in extremities"},
    {"id": "muscle_spasms", "name": "Muscle Spasms", "desc": "Involuntary muscle cramps or twitches"},
    {"id": "back_pain", "name": "Back Pain", "desc": "Ache or stiffness in spine or lower back"},
    {"id": "chest_pain", "name": "Chest Pain", "desc": "Sharp or dull chest pain"},
    {"id": "tremors", "name": "Tremors", "desc": "Involuntary shaking of hands or body"},
    {"id": "poor_coordination", "name": "Poor Coordination", "desc": "Unsteadiness or clumsiness while moving"},
    {"id": "blurred_vision", "name": "Blurred Vision", "desc": "Lack of visual sharpness or clarity"},
    {"id": "double_vision", "name": "Double Vision", "desc": "Diplopia or seeing two images of one object"},
    {"id": "eye_strain", "name": "Eye Strain", "desc": "Fatigue or burning sensation in eyes"},
    {"id": "facial_numbness", "name": "Facial Numbness", "desc": "Reduced feeling in face or cheeks"},

    # Systemic, Gastrointestinal & General Symptoms (41-65)
    {"id": "fatigue", "name": "Fatigue", "desc": "Extreme tiredness or lethargy"},
    {"id": "chills", "name": "Chills", "desc": "Involuntary shivering or feeling cold"},
    {"id": "night_sweats", "name": "Night Sweats", "desc": "Excessive sweating during sleep"},
    {"id": "nausea", "name": "Nausea", "desc": "Sensation of stomach discomfort or urge to vomit"},
    {"id": "vomiting", "name": "Vomiting", "desc": "Involuntary regurgitation of stomach contents"},
    {"id": "diarrhea", "name": "Diarrhea", "desc": "Loose, watery, or frequent bowel movements"},
    {"id": "stomach_cramps", "name": "Stomach Cramps", "desc": "Sharp abdominal pain or spasms"},
    {"id": "loss_of_appetite", "name": "Loss of Appetite", "desc": "Reduced desire to eat or anorexia"},
    {"id": "weight_loss", "name": "Unexplained Weight Loss", "desc": "Noticeable drop in body weight without effort"},
    {"id": "bloating", "name": "Bloating", "desc": "Swollen or tight feeling in abdomen"},
    {"id": "acid_reflux", "name": "Acid Reflux", "desc": "Burning sensation in chest or throat"},
    {"id": "heartburn", "name": "Heartburn", "desc": "Indigestion or upper abdominal heat"},
    {"id": "constipation", "name": "Constipation", "desc": "Infrequent or difficult bowel movements"},
    {"id": "excessive_thirst", "name": "Excessive Thirst", "desc": "Polydipsia or unquenchable thirst"},
    {"id": "dry_mouth", "name": "Dry Mouth", "desc": "Lack of saliva production"},
    {"id": "dehydration", "name": "Dehydration", "desc": "Dry skin, dark urine, and lethargy"},
    {"id": "swollen_lymph_nodes", "name": "Swollen Lymph Nodes", "desc": "Tender lumps in neck, armpits, or groin"},
    {"id": "pale_skin", "name": "Pale Skin", "desc": "Paleness in skin, lips, or nail beds"},
    {"id": "jaundice", "name": "Jaundice", "desc": "Yellowing of skin or eyes"},
    {"id": "flushing", "name": "Flushing", "desc": "Redness or warmth in face and neck"},
    {"id": "cold_sweats", "name": "Cold Sweats", "desc": "Sudden sweating accompanied by chills"},
    {"id": "swollen_feet", "name": "Swollen Feet", "desc": "Fluid retention or edema in ankles/feet"},
    {"id": "dark_urine", "name": "Dark Urine", "desc": "Amber or brownish urine discoloration"},
    {"id": "frequent_urination", "name": "Frequent Urination", "desc": "Urge to urinate more often than usual"},
    {"id": "painful_urination", "name": "Painful Urination", "desc": "Dysuria or burning sensation while urinating"},

    # Skin, Allergy & Dermatological Symptoms (66-85)
    {"id": "skin_rash", "name": "Skin Rash", "desc": "Red, itchy, or irritated patches on skin"},
    {"id": "itching", "name": "Itching", "desc": "Pruritus or persistent desire to scratch"},
    {"id": "hives", "name": "Hives", "desc": "Raised, itchy red welts on skin"},
    {"id": "dry_skin", "name": "Dry Skin", "desc": "Flaky, tight, or cracking skin"},
    {"id": "red_eyes", "name": "Red Eyes", "desc": "Bloodshot or inflamed conjunctiva"},
    {"id": "watery_eyes", "name": "Watery Eyes", "desc": "Excessive tear production"},
    {"id": "swollen_eyelids", "name": "Swollen Eyelids", "desc": "Puffiness or edema around eyes"},
    {"id": "skin_lesions", "name": "Skin Lesions", "desc": "Blisters, bumps, or sores on skin"},
    {"id": "bruising", "name": "Easy Bruising", "desc": "Unexplained purple spots under skin"},
    {"id": "brittle_nails", "name": "Brittle Nails", "desc": "Cracking or splitting fingernails"},
    {"id": "hair_loss", "name": "Hair Loss", "desc": "Thinning hair or excessive shedding"},
    {"id": "excessive_sweating", "name": "Excessive Sweating", "desc": "Hyperhidrosis without heavy exertion"},
    {"id": "peeling_skin", "name": "Peeling Skin", "desc": "Shedding of outer skin layers"},
    {"id": "cold_hands_feet", "name": "Cold Hands & Feet", "desc": "Persistently cold extremities"},
    {"id": "chapped_lips", "name": "Chapped Lips", "desc": "Dry or cracking lips"},
    {"id": "swollen_lips", "name": "Swollen Lips", "desc": "Angioedema or swelling of lips/tongue"},
    {"id": "scalp_itching", "name": "Scalp Itching", "desc": "Irritation or flaking on scalp"},
    {"id": "sun_sensitivity", "name": "Sun Sensitivity", "desc": "Rapid sunburn or rash from sun exposure"},
    {"id": "slow_wound_healing", "name": "Slow Wound Healing", "desc": "Cuts or scrapes taking long to heal"},
    {"id": "skin_redness", "name": "Skin Redness", "desc": "Erythema or inflamed skin zones"},

    # Musculoskeletal, Mood & Sleep Symptoms (86-102)
    {"id": "muscle_weakness", "name": "Muscle Weakness", "desc": "Difficulty lifting or exerting force"},
    {"id": "stiff_joints", "name": "Stiff Joints", "desc": "Reduced range of motion in knees or fingers"},
    {"id": "restlessness", "name": "Restlessness", "desc": "Inability to sit still or relax"},
    {"id": "insomnia", "name": "Insomnia", "desc": "Difficulty falling or staying asleep"},
    {"id": "excessive_sleepiness", "name": "Excessive Sleepiness", "desc": "Somnolence or drowsing during daylight"},
    {"id": "anxiety", "name": "Anxiety", "desc": "Persistent worry, nervousness, or dread"},
    {"id": "mood_swings", "name": "Mood Swings", "desc": "Rapid shifts in emotion or irritability"},
    {"id": "brain_fog", "name": "Brain Fog", "desc": "Sluggish thinking or lack of mental clarity"},
    {"id": "heart_palpitations", "name": "Heart Palpitations", "desc": "Fluttering, racing, or pounding heartbeat"},
    {"id": "short_breath_exertion", "name": "Shortness of Breath on Exertion", "desc": "Breathlessness during mild exercise"},
    {"id": "leg_cramps", "name": "Leg Cramps", "desc": "Sudden painful tightness in calf muscle"},
    {"id": "swollen_joints", "name": "Swollen Joints", "desc": "Visible enlargement or fluid around joints"},
    {"id": "postural_dizziness", "name": "Postural Dizziness", "desc": "Dizziness upon standing up quickly"},
    {"id": "cold_intolerance", "name": "Cold Intolerance", "desc": "Abnormal sensitivity to cold environments"},
    {"id": "heat_intolerance", "name": "Heat Intolerance", "desc": "Inability to tolerate warm temperatures"},
    {"id": "snoring", "name": "Snoring", "desc": "Loud breathing noise during sleep"},
    {"id": "daytime_fatigue", "name": "Daytime Fatigue", "desc": "Persistent tiredness despite full sleep"}
]

KNOWLEDGE_BASE = {
    "Common Cold": {
        "symptoms": ["sneezing", "sore_throat", "runny_nose", "nasal_congestion", "cough", "post_nasal_drip"],
        "description": "Mild viral upper respiratory tract infection affecting nasal passages and throat.",
        "precaution": "Stay hydrated, rest adequately, wash hands frequently, and avoid touching face.",
        "cure": "Over-the-counter antihistamines, saline nasal sprays, warm fluids, and vitamin C."
    },
    "Influenza (Flu)": {
        "symptoms": ["fever", "body_pain", "fatigue", "cough", "chills", "headache", "muscle_weakness"],
        "description": "Contagious respiratory illness caused by influenza viruses.",
        "precaution": "Annual flu vaccination, isolate to prevent spread, wear masks, sanitise surfaces.",
        "cure": "Antiviral medication (if prescribed early), paracetamol for fever, bed rest, and fluids."
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "shortness_of_breath", "fatigue", "loss_of_smell", "loss_of_taste", "chest_tightness"],
        "description": "Viral infection caused by SARS-CoV-2 targeting upper and lower respiratory pathways.",
        "precaution": "Self-isolate immediately, monitor oxygen levels, wear N95 masks, maintain distance.",
        "cure": "Consult medical practitioner, supportive oxygen therapy if needed, antipyretics, and rest."
    },
    "Migraine": {
        "symptoms": ["headache", "fatigue", "sensitivity_to_light", "sensitivity_to_sound", "nausea", "blurred_vision"],
        "description": "Neurological condition causing intense throbbing head pain, usually on one side.",
        "precaution": "Avoid loud noises/bright lights, identify dietary triggers, manage daily stress.",
        "cure": "Rest in a quiet dark room, cold compresses, prescribed triptans or pain relievers."
    },
    "Acute Bronchitis": {
        "symptoms": ["cough", "shortness_of_breath", "body_pain", "chest_tightness", "wheezing", "hoarseness"],
        "description": "Inflammation of the lining of your bronchial tubes carrying air to lungs.",
        "precaution": "Avoid smoke and air pollutants, use a humidifier, practice deep breathing exercises.",
        "cure": "Cough suppressants, bronchodilators, warm steam inhalation, and hydration."
    },
    "Allergic Rhinitis": {
        "symptoms": ["sneezing", "runny_nose", "headache", "watery_eyes", "red_eyes", "itching", "post_nasal_drip"],
        "description": "Allergic response causing nasal inflammation, watery eyes, and continuous sneezing.",
        "precaution": "Avoid known allergens (pollen, dust, dander), keep windows closed in high pollen seasons.",
        "cure": "Antihistamines, nasal corticosteroid sprays, and allergen avoidance."
    },
    "Gastroenteritis (Stomach Flu)": {
        "symptoms": ["nausea", "vomiting", "diarrhea", "stomach_cramps", "fever", "dehydration", "loss_of_appetite"],
        "description": "Intestinal infection marked by watery diarrhea, cramps, nausea, and fever.",
        "precaution": "Drink oral rehydration solutions (ORS), wash hands thoroughly, avoid solid foods initially.",
        "cure": "Electrolyte replenishment, anti-diarrheal agents if recommended, light bland diet."
    },
    "Sinusitis (Sinus Infection)": {
        "symptoms": ["sinus_pressure", "headache", "nasal_congestion", "runny_nose", "sore_throat", "post_nasal_drip"],
        "description": "Inflammation or swelling of the tissue lining the sinuses.",
        "precaution": "Use nasal saline rinses, apply warm compresses over face, stay well hydrated.",
        "cure": "Nasal decongestants, warm steam inhalation, pain relievers, or antibiotics if bacterial."
    },
    "Asthma Exacerbation": {
        "symptoms": ["wheezing", "shortness_of_breath", "chest_tightness", "cough", "rapid_breathing"],
        "description": "Condition in which airways narrow, swell, and produce extra mucus.",
        "precaution": "Avoid cold air, dust, and smoke; carry rescue inhalers at all times.",
        "cure": "Inhaled corticosteroids, quick-relief bronchodilators (albuterol), medical monitoring."
    },
    "Streptococcal Pharyngitis (Strep Throat)": {
        "symptoms": ["sore_throat", "fever", "swollen_lymph_nodes", "headache", "loss_of_appetite", "body_pain"],
        "description": "Bacterial throat infection causing severe pain and inflammation.",
        "precaution": "Replace toothbrush after starting treatment, gargle warm salt water, avoid sharing utensils.",
        "cure": "Prescribed oral antibiotics (amoxicillin/penicillin), throat lozenges, analgesics."
    },
    "Hypertension (High Blood Pressure)": {
        "symptoms": ["headache", "dizziness", "blurred_vision", "heart_palpitations", "shortness_of_breath"],
        "description": "Common condition in which long-term force of blood against artery walls is high.",
        "precaution": "Reduce dietary sodium intake, exercise regularly, manage stress levels.",
        "cure": "Antihypertensive medications (ACE inhibitors, beta-blockers), lifestyle modifications."
    },
    "Iron Deficiency Anemia": {
        "symptoms": ["fatigue", "pale_skin", "dizziness", "cold_hands_feet", "brittle_nails", "muscle_weakness", "brain_fog"],
        "description": "Condition where blood lacks adequate healthy red blood cells due to insufficient iron.",
        "precaution": "Consume iron-rich foods (spinach, lentils, red meat), combine with Vitamin C for absorption.",
        "cure": "Oral iron supplements, dietary adjustments, and treating underlying blood loss causes."
    },
    "Urinary Tract Infection (UTI)": {
        "symptoms": ["painful_urination", "frequent_urination", "dark_urine", "fever", "stomach_cramps", "back_pain"],
        "description": "Infection in any part of the urinary system, most commonly the bladder and urethra.",
        "precaution": "Drink plenty of water daily, practice good personal hygiene, do not delay urination.",
        "cure": "Prescribed oral antibiotics, urinary analgesics, and increased water consumption."
    },
    "Tension Headache": {
        "symptoms": ["headache", "neck_stiffness", "body_pain", "eye_strain", "fatigue"],
        "description": "Mild to moderate pain often described as feeling like a tight band around the head.",
        "precaution": "Practice muscle relaxation techniques, take regular computer breaks, maintain good posture.",
        "cure": "Over-the-counter pain relievers (ibuprofen/paracetamol), stress reduction, rest."
    },
    "Gastroesophageal Reflux (GERD)": {
        "symptoms": ["acid_reflux", "heartburn", "chest_pain", "hoarseness", "sore_throat", "bloating"],
        "description": "Digestive disease in which stomach acid or bile irritates the food pipe lining.",
        "precaution": "Avoid lying down immediately after meals, limit spicy/fatty foods, elevate head of bed.",
        "cure": "Antacids, H2 blockers, proton pump inhibitors (PPIs), and dietary management."
    },
    "Generalized Anxiety Disorder": {
        "symptoms": ["anxiety", "restlessness", "insomnia", "heart_palpitations", "muscle_spasms", "brain_fog"],
        "description": "Persistent and excessive worry about everyday activities accompanied by physical tension.",
        "precaution": "Practice mindfulness and deep breathing exercises, limit caffeine and alcohol intake.",
        "cure": "Cognitive Behavioral Therapy (CBT), stress management, prescribed anti-anxiety treatments."
    },
    "Hypothyroidism": {
        "symptoms": ["fatigue", "cold_intolerance", "dry_skin", "brittle_nails", "muscle_weakness", "brain_fog", "stiff_joints"],
        "description": "Underactive thyroid gland failing to produce sufficient crucial thyroid hormones.",
        "precaution": "Maintain regular thyroid function blood tests, follow consistent daily medication timing.",
        "cure": "Daily synthetic thyroid hormone replacement (levothyroxine)."
    },
    "Dermatitis / Eczema": {
        "symptoms": ["skin_rash", "itching", "dry_skin", "skin_redness", "peeling_skin", "hives"],
        "description": "Non-contagious skin inflammation causing itchy, red, dry, or cracked skin patches.",
        "precaution": "Moisturize skin twice daily, avoid harsh soaps, wear soft breathable cotton clothing.",
        "cure": "Topical corticosteroid creams, soothing emollient moisturizers, antihistamines for itching."
    }
}