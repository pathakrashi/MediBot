from knowledge_base import KNOWLEDGE_BASE

def run_forward_chaining(reported_symptoms):
    matched_rules = []
    diagnoses = []
    details = []
    
    if not reported_symptoms:
        return {
            "matched_rules": [],
            "diagnoses": [],
            "details": []
        }
        
    for disease, data in KNOWLEDGE_BASE.items():
        matching_symptoms = [s for s in data["symptoms"] if s in reported_symptoms]
        
        if len(matching_symptoms) > 0:
            match_pct = int((len(matching_symptoms) / len(data["symptoms"])) * 100)
            
            matched_rules.append(f"RULE: {disease} ({match_pct}% Match)")
            diagnoses.append(f"{disease} ({match_pct}%)")
            
            details.append({
                "disease": disease,
                "description": data["description"],
                "precaution": data["precaution"],
                "cure": data["cure"],
                "match_count": len(matching_symptoms),
                "total_symptoms": len(data["symptoms"]),
                "match_pct": match_pct
            })
            
    details.sort(key=lambda x: x["match_pct"], reverse=True)
    
    return {
        "matched_rules": matched_rules,
        "diagnoses": diagnoses,
        "details": details
    }

def run_backward_chaining(target_disease, reported_symptoms):
    if target_disease not in KNOWLEDGE_BASE:
        return {
            "is_verified": False, 
            "has_input": False,
            "required_symptoms": [], 
            "missing_symptoms": [], 
            "present_symptoms": [],
            "match_pct": 0,
            "details": None
        }
        
    data = KNOWLEDGE_BASE[target_disease]
    required = data["symptoms"]
    
    present_symptoms = [s for s in required if s in reported_symptoms] if reported_symptoms else []
    missing = [s for s in required if s not in present_symptoms]
    
    match_pct = int((len(present_symptoms) / len(required)) * 100) if required else 0
    is_verified = len(present_symptoms) > 0
    
    return {
        "is_verified": is_verified,
        "has_input": bool(reported_symptoms),
        "required_symptoms": required,
        "missing_symptoms": missing,
        "present_symptoms": present_symptoms,
        "match_pct": match_pct,
        "details": {
            "disease": target_disease,
            "description": data["description"],
            "precaution": data["precaution"],
            "cure": data["cure"]
        }
    }