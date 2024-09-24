import random
import gradio as gr
from nltk.stem import WordNetLemmatizer

# Initialize the WordNet Lemmatizer
lemmatizer = WordNetLemmatizer()

# Define a dictionary for greetings, self-introduction, farewell,
# response to "thank you," and asking about the user's well-being
responses = {
    'greetings': [
        "Hello! How can I assist you today?",
        "Hi there! How can I help you?",
        "Greetings! How may I assist you?",
        "Good day! How can I help you today?",
        "Hey! How may I assist you?"
    ],
    'introduction': "My name is MedBot. I'm here to help with medical information.",
    'farewell': "Goodbye! Take care of yourself and feel free to come back if you have more questions.",
    'thank_you': "You're welcome! If you have any more questions, feel free to ask.",
    'well_being': [
        "I'm doing great! How may I help you today?",
        "I'm doing well, thank you! How can I assist you today?",
    ],
    'ask_symptoms': "I'm sorry to hear that you're feeling sick. Could you please describe your symptoms?"
}

# Define a dictionary of diseases, symptoms, treatments, and healthcare facilities
diseases = {
    'flu': {
        'symptoms': ['fever', 'cough', 'sore throat'],
        'description': "Influenza, commonly known as the flu, "
                       "is a contagious respiratory illness caused by influenza viruses. "
                       "It can cause mild to severe illness.",
        'treatments': ['Rest and fluid intake', 'Antiviral medication'],
        'facilities': ['Hospital A', 'Clinic B']
    },
    'malaria': {
        'symptoms': ['fever', 'chills', 'headache'],
        'description': "Malaria is a mosquito-borne infectious disease that affects humans and other animals."
                       " It causes symptoms such as fever, chills, and headache.",
        'treatments': ['Antimalarial medication', 'Bed rest'],
        'facilities': ['Hospital C', 'Clinic D']
    },
    'COVID-19': {
        'symptoms': ['fever', 'cough', 'shortness of breath'],
        'description': "COVID-19 is a highly contagious respiratory illness caused by the SARS-CoV-2 virus. "
                       "It can cause mild to severe respiratory symptoms and has led to a global pandemic.",
        'treatments': ['Isolation', 'Symptomatic treatment'],
        'facilities': ['Hospital E', 'Urgent Care Center F']
    },
    'common cold': {
        'symptoms': ['runny nose', 'sneezing', 'cough'],
        'description': "The common cold is a viral infection that primarily affects the nose and throat. "
                       "It is characterized by symptoms such as a runny nose, sneezing, and cough.",
        'treatments': ['Rest', 'Fluids', 'Over-the-counter medication'],
        'facilities': ['Clinic G', 'Pharmacy H']
    },
    'asthma': {
        'symptoms': ['shortness of breath', 'wheezing', 'chest tightness'],
        'description': "Asthma is a chronic respiratory condition "
                       "that causes inflammation and narrowing of the airways. "
                       "It leads to symptoms such as shortness of breath, wheezing, and chest tightness.",
        'treatments': ['Inhaled medications', 'Lifestyle modifications'],
        'facilities': ['Hospital I', 'Specialist Clinic J']
    },
    'diabetes': {
        'symptoms': ['frequent urination', 'increased thirst', 'fatigue'],
        'description': "Diabetes is a chronic condition that affects how the body regulates blood sugar levels. "
                       "Common symptoms include frequent urination, increased thirst, and fatigue.",
        'treatments': ['Insulin therapy', 'Medication', 'Lifestyle changes'],
        'facilities': ['Diabetes Center K', 'Endocrinology Clinic L']
    },
    'hypertension': {
        'symptoms': ['high blood pressure', 'headache', 'dizziness'],
        'description': "Hypertension, or high blood pressure,"
                       " is a chronic condition characterized by elevated blood pressure levels. "
                       "It often presents with symptoms such as headaches and dizziness.",
        'treatments': ['Medication', 'Lifestyle modifications'],
        'facilities': ['Cardiology Clinic M', 'Internal Medicine Clinic N']
    },
    'allergies': {
        'symptoms': ['sneezing', 'itchy eyes', 'nasal congestion'],
        'description': "Allergies occur when the immune system overreacts to substances that are usually harmless. "
                       "Common symptoms include sneezing, itchy eyes, and nasal congestion.",
        'treatments': ['Antihistamines', 'Nasal sprays'],
        'facilities': ['Allergy Clinic O', 'ENT Clinic P']
    },
    'gastroenteritis': {
        'symptoms': ['nausea', 'vomiting', 'diarrhea'],
        'description': "Gastroenteritis, also known as stomach flu, is an inflammation of the stomach and intestines. "
                       "It typically causes symptoms such as nausea, vomiting, and diarrhea.",
        'treatments': ['Fluid replacement', 'Symptomatic relief'],
        'facilities': ['Gastroenterology Clinic Q', 'Urgent Care Center R']
    },
    'pneumonia': {
        'symptoms': ['cough', 'fever', 'chest pain'],
        'description': "Pneumonia is an infection that inflames the air sacs in one or both lungs. "
                       "Common symptoms include cough, fever, and chest pain.",
        'treatments': ['Antibiotics', 'Rest', 'Fluids'],
        'facilities': ['Hospital S', 'Pulmonology Clinic T']
    },
    'urinary tract infection': {
        'symptoms': ['frequent urination', 'burning sensation', 'abdominal pain'],
        'description': "A urinary tract infection (UTI) is an infection in any part "
                       "of the urinary system, including the kidneys, bladder, and urethra. "
                       "It often presents with symptoms such as frequent urination, "
                       "a burning sensation, and abdominal pain.",
        'treatments': ['Antibiotics', 'Increased fluid intake'],
        'facilities': ['Urology Clinic U', 'Internal Medicine Clinic V']
    },
    'migraine': {
        'symptoms': ['severe headache', 'nausea', 'sensitivity to light'],
        'description': "Migraine is a neurological condition characterized by recurrent, severe headaches. "
                       "Common symptoms include a severe headache, nausea, and sensitivity to light.",
        'treatments': ['Pain medication', 'Lifestyle modifications'],
        'facilities': ['Neurology Clinic W', 'Headache Center X']
    },
    'bronchitis': {
        'symptoms': ['cough', 'phlegm', 'chest discomfort'],
        'description': "Bronchitis is an inflammation of the bronchial tubes, which carry air to and from the lungs. "
                       "It typically causes symptoms such as a cough, phlegm production, and chest discomfort.",
        'treatments': ['Rest', 'Fluids', 'Cough medication'],
        'facilities': ['Respiratory Clinic Y', 'Internal Medicine Clinic Z']
    },
    'gastritis': {
        'symptoms': ['abdominal pain', 'nausea', 'indigestion'],
        'description': "Gastritis is inflammation of the lining of the stomach. "
                       "Common symptoms include abdominal pain, nausea, and indigestion.",
        'treatments': ['Antacids', 'Dietary changes'],
        'facilities': ['Gastroenterology Clinic AA', 'Internal Medicine Clinic BB']
    },
    'osteoporosis': {
        'symptoms': ['bone pain', 'fractures', 'loss of height'],
        'description': "Osteoporosis is a condition characterized by low bone density and increased risk of fractures. "
                       "Symptoms include bone pain, fractures, and loss of height.",
        'treatments': ['Calcium supplements', 'Vitamin D supplements', 'Medication'],
        'facilities': ['Rheumatology Clinic CC', 'Orthopedic Clinic DD']
    },
    'depression': {
        'symptoms': ['persistent sadness', 'loss of interest', 'low energy'],
        'description': "Depression is a mental health disorder characterized by persistent sadness, "
                       "loss of interest, and feelings of low energy.",
        'treatments': ['Therapy', 'Medication', 'Lifestyle changes'],
        'facilities': ['Psychiatry Clinic EE', 'Mental Health Center FF']
    },
    'anxiety': {
        'symptoms': ['excessive worry', 'restlessness', 'difficulty concentrating'],
        'description': "Anxiety is a mental health disorder characterized by excessive worry, "
                       "restlessness, and difficulty concentrating.",
        'treatments': ['Therapy', 'Medication', 'Relaxation techniques'],
        'facilities': ['Psychology Clinic GG', 'Mental Health Center HH']
    }
    # Add more diseases, symptoms, treatments, and corresponding facilities as needed
}


# Function to lemmatize a word
def lemmatize_word(word):
    return lemmatizer.lemmatize(word.lower())


def diagnose_disease(user_input):
    user_input = user_input.lower()
    user_symptoms = set(lemmatize_word(symptom) for symptom in user_input.split())
    disease_scores = {}

    for disease, disease_info in diseases.items():
        disease_symptoms = set(disease_info['symptoms'])
        score = len(user_symptoms.intersection(disease_symptoms))
        disease_scores[disease] = score

    matched_diseases = [disease for disease, score in disease_scores.items() if score > 0]

    if matched_diseases:
        max_score = max(disease_scores[disease] for disease in matched_diseases)
        possible_diseases = [disease for disease, score in disease_scores.items() if score == max_score]

        return possible_diseases
    else:
        # Check for diseases that have at least one symptom matching a multi-word symptom in the user input
        matched_diseases = []
        for disease, disease_info in diseases.items():
            for symptom in disease_info['symptoms']:
                if any(word in user_input.split() for word in symptom.split()):
                    matched_diseases.append(disease)
                    break

        return matched_diseases if matched_diseases else ['unknown']


# Function to provide treatment information for the diagnosed disease
def provide_treatment(disease):
    return diseases[disease]['treatments'] if disease in diseases else "unknown"


# Function to refer to a healthcare facility
def refer_to_facility(disease):
    return random.choice(diseases[disease]['facilities']) \
        if disease in diseases else 'Komfo Anokye Teaching Hospital - Kumasi'


# Function to handle the chatbot interaction
def chatbot_interaction(user_input):
    if any(greeting in user_input.lower() for greeting in
           ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening', 'good day', 'what\'s up']):
        return random.choice(responses['greetings'])

    if 'name' in user_input.lower() and 'your' in user_input.lower():
        return responses['introduction']

    if any(farewell in user_input.lower() for farewell in ['goodbye', 'bye']):
        return responses['farewell']

    if 'thank you' in user_input.lower() or 'thanks' in user_input.lower():
        return responses['thank_you']

    if 'how are you' in user_input.lower():
        return random.choice(responses['well_being'])

    if 'sick' in user_input.lower() or 'ill' in user_input.lower() or 'not feeling well' in user_input.lower():
        return responses['ask_symptoms']

    diagnosis = diagnose_disease(user_input)

    if isinstance(diagnosis, list) and len(diagnosis) > 0:
        # Randomly select one disease from the list of possible diseases
        disease = random.choice(diagnosis)

        response = f"The possible disease based on your symptoms is: {disease}"

        if disease in diseases:
            description = diseases[disease]['description']
            response += f"\n\nDescription: {description}"

            facility = refer_to_facility(disease)
            response += f"\n\nFor {disease}, you may consider visiting {facility}."

            treatments = provide_treatment(disease)
            response += f"\n\nThe recommended treatments for {disease} include:\n"
            response += "\n".join(treatments)
        else:
            response += "\n\nI'm sorry, I couldn't find detailed information about the disease."

    else:
        response = "I'm sorry, I couldn't determine the disease based on the symptoms provided."
        facility = refer_to_facility('unknown')
        response += f"\n\nYou may consider visiting {facility} for further evaluation."

    return response


iface = gr.Interface(
    fn=chatbot_interaction,
    inputs="text",
    outputs="text",
    title="Medical Chatbot",
    description="Chat with MedBot, a medical chatbot that can assist you with symptoms,"
                " diseases, treatments, and healthcare facilities.",
    examples=[
        ["What are the common treatments for a headache?"],
        ["I have a cough and fever, what could be the possible diseases?"],
        ["Thank you for the information."]
    ]
)

iface.launch(share=True)
