import streamlit as st
import pickle
import pandas as pd

# Load CSS
#with open('css/style.css') as f:
 #   st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load medicine data
medicines_dict = pickle.load(open('medicine_dict.pkl', 'rb'))
medicines = pd.DataFrame(medicines_dict)

# Load similarity vector data
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend_medication(symptoms_or_disease):
    recommended_medications = []
    for item in symptoms_or_disease:
        item = item.strip().lower()  # Convert to lowercase and remove leading/trailing spaces
        if item in medicines.columns:
            matched_medications = medicines.loc[medicines[item].notna(), item].tolist()
            recommended_medications.extend(matched_medications)
    return list(set(recommended_medications))

def display_disease_symptoms():
    st.sidebar.subheader("Disease Symptoms")
    st.sidebar.write("Here are some common diseases along with their symptoms and recommended medications:")
    disease_symptoms = {
        "Common Cold": {
            "Symptoms": ["Runny Nose", "Sore Throat", "Cough", "Fever"],
            "Medications": ["Paracetamol", "Ibuprofen"],
            "Purchase Link": "https://pharmeasy.in/"
        },
        "Influenza": {
            "Symptoms": ["Fever", "Muscle Pain", "Headache", "Cough"],
            "Medications": ["Tamiflu", "Relenza"],
            "Purchase Link": "https://pharmeasy.in/"},
                             "Allergies": {
        "Symptoms": ["Runny Nose", "Sneezing", "Itchy Eyes", "Skin Rash"],
        "Medications": ["Cetirizine", "Loratadine"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Pneumonia": {
        "Symptoms": ["Fever", "Cough", "Shortness of Breath", "Chest Pain"],
        "Medications": ["Antibiotics", "Bronchodilators"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Strep Throat": {
        "Symptoms": ["Sore Throat", "Fever", "Swollen Tonsils", "Painful Swallowing"],
        "Medications": ["Penicillin", "Amoxicillin"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Sinusitis": {
        "Symptoms": ["Nasal Congestion", "Facial Pain", "Headache", "Runny Nose"],
        "Medications": ["Decongestants", "Steroid Nasal Sprays"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Gastroenteritis": {
        "Symptoms": ["Nausea", "Vomiting", "Diarrhea", "Stomach Pain"],
        "Medications": ["Oral Rehydration Solutions", "Antidiarrheal Medications"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Urinary Tract Infection": {
        "Symptoms": ["Frequent Urination", "Painful Urination", "Cloudy Urine", "Lower Abdominal Pain"],
        "Medications": ["Antibiotics", "Pain Relievers"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Migraine": {
        "Symptoms": ["Severe Headache", "Nausea", "Sensitivity to Light", "Throbbing Pain"],
        "Medications": ["Triptans", "Ergotamines"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Asthma": {
        "Symptoms": ["Shortness of Breath", "Wheezing", "Coughing", "Chest Tightness"],
        "Medications": ["Inhaled Corticosteroids", "Short-Acting Beta Agonists"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Hypertension": {
        "Symptoms": ["High Blood Pressure", "Headache", "Dizziness", "Chest Pain"],
        "Medications": ["ACE Inhibitors", "Calcium Channel Blockers"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Diabetes": {
        "Symptoms": ["Frequent Urination", "Excessive Thirst", "Fatigue", "Unexplained Weight Loss"],
        "Medications": ["Metformin", "Insulin"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Osteoarthritis": {
        "Symptoms": ["Joint Pain", "Stiffness", "Swelling", "Decreased Range of Motion"],
        "Medications": ["Acetaminophen", "NSAIDs"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Anxiety": {
        "Symptoms": ["Excessive Worry", "Restlessness", "Fatigue", "Difficulty Concentrating"],
        "Medications": ["SSRIs", "Benzodiazepines"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Depression": {
        "Symptoms": ["Persistent Sadness", "Loss of Interest", "Fatigue", "Difficulty Sleeping"],
        "Medications": ["SSRIs", "SNRIs"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Hyperthyroidism": {
        "Symptoms": ["Weight Loss", "Rapid Heartbeat", "Anxiety", "Excessive Sweating"],
        "Medications": ["Beta Blockers", "Antithyroid Drugs"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Hypothyroidism": {
        "Symptoms": ["Weight Gain", "Fatigue", "Dry Skin", "Constipation"],
        "Medications": ["Levothyroxine", "Liothyronine"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Chronic Kidney Disease": {
        "Symptoms": ["Fatigue", "Swelling", "Shortness of Breath", "Decreased Appetite"],
        "Medications": ["ACE Inhibitors", "Angiotensin II Receptor Blockers"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Rheumatoid Arthritis": {
        "Symptoms": ["Joint Pain", "Swelling", "Stiffness", "Fatigue"],
        "Medications": ["Disease-Modifying Antirheumatic Drugs", "Biologic Response Modifiers"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Chronic Obstructive Pulmonary Disease (COPD)": {
        "Symptoms": ["Shortness of Breath", "Chronic Cough", "Wheezing", "Chest Tightness"],
        "Medications": ["Bronchodilators", "Inhaled Corticosteroids"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Heart Failure": {
        "Symptoms": ["Shortness of Breath", "Fatigue", "Swelling", "Rapid Heartbeat"],
        "Medications": ["ACE Inhibitors", "Beta Blockers"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Epilepsy": {
        "Symptoms": ["Seizures", "Loss of Consciousness", "Confusion", "Muscle Stiffness"],
        "Medications": ["Anticonvulsants", "Benzodiazepines"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Gout": {
        "Symptoms": ["Joint Pain", "Swelling", "Redness", "Heat"],
        "Medications": ["NSAIDs", "Colchicine"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Acid Reflux": {
        "Symptoms": ["Heartburn", "Regurgitation", "Nausea", "Chest Pain"],
        "Medications": ["Proton Pump Inhibitors", "H2 Receptor Antagonists"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Anemia": {
        "Symptoms": ["Fatigue", "Weakness", "Pale Skin", "Shortness of Breath"],
        "Medications": ["Iron Supplements", "Vitamin B12 Supplements"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Psoriasis": {
        "Symptoms": ["Red Patches", "Thickened Skin", "Silver Scales", "Itching"],
        "Medications": ["Topical Corticosteroids", "Vitamin D Analogues"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Hyperlipidemia": {
        "Symptoms": ["High Cholesterol Levels", "Chest Pain", "Heart Attack", "Stroke"],
        "Medications": ["Statins", "Fibrates"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Malaria": {
        "Symptoms": ["Fever", "Chills", "Headache", "Nausea"],
        "Medications": ["Chloroquine", "Artemisinin Combination Therapies"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Osteoporosis": {
        "Symptoms": ["Bone Fractures", "Back Pain", "Loss of Height", "Stooped Posture"],
        "Medications": ["Bisphosphonates", "Calcium Supplements"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Insomnia": {
        "Symptoms": ["Difficulty Falling Asleep", "Difficulty Staying Asleep", "Daytime Sleepiness", "Irritability"],
        "Medications": ["Benzodiazepines", "Non-Benzodiazepine Hypnotics"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Eczema": {
        "Symptoms": ["Itching", "Redness", "Dry Skin", "Rashes"],
        "Medications": ["Topical Corticosteroids", "Emollients"],
        "Purchase Link": "https://pharmeasy.in/"
    },
    "Hepatitis": {
        "Symptoms": ["Fatigue", "Jaundice", "Abdominal Pain", "Nausea"],
        "Medications": ["Antiviral Medications", "Interferons"],
        "Purchase Link": "https://pharmeasy.in/"}



        # Add more diseases and symptoms here
    }
    for disease, info in disease_symptoms.items():
        st.sidebar.write(f"**{disease}:**")
        st.sidebar.write("**Symptoms:**")
        for symptom in info["Symptoms"]:
            st.sidebar.write(f"- {symptom}")
        st.sidebar.write("**Recommended Medications:**")
        for medication in info["Medications"]:
            st.sidebar.write(f"- {medication}")
        st.sidebar.write(f"**Purchase Medications:** [Purchase Here]({info['Purchase Link']})")

def main():
    st.title('Medicine Recommendation System')
    display_disease_symptoms()
    symptoms_input = st.text_input("Enter your symptoms or disease separated by commas (e.g., fever, headache, cough):")
    if not symptoms_input:
        st.warning("Please enter at least one symptom or disease.")
        st.stop()

    symptoms_or_disease = [item.strip().lower() for item in symptoms_input.split(",")]

    recommended_medications = recommend_medication(symptoms_or_disease)

    if recommended_medications:
        st.success("Based on your symptoms or disease, we recommend the following medication(s):")
        for idx, med_name in enumerate(recommended_medications, 1):
            st.write(f"{idx}. {med_name}")
            st.write(f"Click here to buy: [PharmEasy](https://pharmeasy.in/search/all?name={med_name})")
    #else:
        #st.warning("No medications found for the selected symptoms or disease. Please consult a healthcare professional.")

if __name__ == '__main__':
    main()
