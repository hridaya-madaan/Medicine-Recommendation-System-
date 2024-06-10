
ChatGPT
Medicine Recommendation System 💊
This recommendation system suggests medicines or drugs based on user input. It aims to provide alternatives or substitutes for the searched medication.

Features
User-Friendly Interface: Simple input for symptoms and health conditions.
Personalized Recommendations: Tailored suggestions using machine learning algorithms.
Comprehensive Medication Database: Detailed information about medications.
Secure and Confidential: Ensures user data privacy.
Online Pharmacy Links: Directs users to purchase recommended medications online.
Steps to Open Localhost for Application: 🌐
Clone GitHub Repository:

sh
Copy code
git clone https://github.com/your-repo/Medicine-Recommendation-System.git
cd Medicine-Recommendation-System
Extract pickle-files.rar:

Ensure similarity.pkl and medicine_dict.pkl are in the root directory with app.py.
Download and Open Pycharm IDE:

Open this application folder in Pycharm.
Open Terminal.

Install Required Libraries:

sh
Copy code
pip install streamlit pandas pickle
Run the Application:

sh
Copy code
streamlit run app.py
If the application does not start, try:
sh
Copy code
python -m streamlit run app.py
Note: If the terminal throws an error "streamlit is not recognized as an internal or external command", recreate a new Python project, import all libraries, and include the CSS & images folder along with the extracted pickle files.

Deployment and Data Files 📦
To facilitate deployment and address GitHub's file size limit of 100 MB, we have reduced the size of the similarity.pkl file. However, the original data files required for the application are available in the pickle-files.rar archive.

Reduced similarity.pkl File: Provided in the root directory, optimized for deployment with a smaller subset of data.

Original Data Files: Extract similarity.pkl and medicine_dict.pkl from pickle-files.rar for full functionality. Ensure they are placed in the same directory as app.py.

You can extract the files using tools such as WinRAR, 7-Zip, or the unrar command-line utility.

Ensure the extracted data files are present in the root directory alongside app.py to ensure the application works with the complete dataset.

Picture Demonstration ▶


Example Code Snippet
python
Copy code
from flask import Flask, request, jsonify, redirect
import pandas as pd
import numpy as np
import joblib

# Load pre-trained model and medication database
model = joblib.load("model.pkl")
medication_db = pd.read_csv("medication_database.csv")

app = Flask(__name__)

def preprocess(symptoms):
    # Dummy preprocessing function
    return np.array([symptoms.get('fever', 0), symptoms.get('cough', 0)])

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    symptoms = data['symptoms']
    
    # Preprocess user input
    user_input = preprocess(symptoms)
    
    # Predict the best medication
    prediction = model.predict([user_input])
    recommended_med = medication_db.loc[prediction[0]]
    
    return jsonify({
        'medication': recommended_med['name'],
        'details': recommended_med['details'],
        'link': recommended_med['purchase_link']
    })

if __name__ == '__main__':
    app.run(debug=True)
By following these instructions, you can deploy the application with the reduced similarity.pkl file while having access to the original data files when needed



