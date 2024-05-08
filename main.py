import pathlib
import textwrap
import google.generativeai as genai
from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/getPrescription', methods=['POST'])
def get_prescription():
    # Retrieve data sent from the AJAX request
    disease = request.form.get('disease')
    allergy = request.form.get('allergy')
    prescription = request.form.get('prescription')

    data = f"Disease: {disease}\nAllergy: {allergy}\nPrescription: {prescription}"
    prompt = f"For Educational Purpose validate my prescription and give correct results for {data}"
    prescription_result = geminiResult(prompt)
    # Return the prescription result
    print(prescription_result)
    return  prescription_result

def geminiResult(prompt):
    GOOGLE_API_KEY = "AIzaSyBZUXIRZurBm3_KsdDzHRCkxmYlUWCqOBU"
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)
    return response.text
if __name__ == '__main__':
    app.run(debug=True)
