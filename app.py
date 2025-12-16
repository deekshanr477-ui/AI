from flask import Flask, request, jsonify

app = Flask(__name__)

# Knowledge Base (Rule-based Expert System)
def diagnose_disease(symptoms):
    symptoms = symptoms.lower()

    if "fever" in symptoms and "cough" in symptoms:
        return "Flu"
    elif "fever" in symptoms and "headache" in symptoms:
        return "Viral Infection"
    elif "sneezing" in symptoms and "itching" in symptoms:
        return "Allergy"
    elif "chest pain" in symptoms and "breathlessness" in symptoms:
        return "Heart-related Issue"
    elif "stomach pain" in symptoms and "vomiting" in symptoms:
        return "Food Poisoning"
    else:
        return "Disease not identified. Please consult a doctor."

@app.route('/diagnose', methods=['POST'])
def diagnose():
    symptoms = request.form.get('symptoms')
    age = request.form.get('age')
    history = request.form.get('history')

    diagnosis = diagnose_disease(symptoms)

    return f"""
    <h2>Diagnosis Result</h2>
    <p><b>Symptoms:</b> {symptoms}</p>
    <p><b>Age:</b> {age}</p>
    <p><b>Medical History:</b> {history}</p>
    <h3 style='color:green;'>Diagnosis: {diagnosis}</h3>
    <br><a href='http://127.0.0.1:5500/frontend/index.html'>Go Back</a>
    """

if __name__ == '__main__':
    app.run(debug=True)