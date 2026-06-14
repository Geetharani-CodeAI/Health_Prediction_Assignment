import google.generativeai as genai

genai.configure(api_key="API_Key")

model = genai.GenerativeModel("gemini-2.5-flash-lite")


def generate_remarks(disease_risk, glucose, haemoglobin, cholesterol):

    prompt = f"""
    You are a healthcare assistant.

    Disease Risk: {disease_risk}
    Glucose: {glucose}
    Haemoglobin: {haemoglobin}
    Cholesterol: {cholesterol}

    Generate a short medical remark in 1-2 sentences.
    """

    response = model.generate_content(prompt)

    return response.text
