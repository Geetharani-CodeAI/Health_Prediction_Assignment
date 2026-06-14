import streamlit as st
import pickle
import pandas as pd
import re
from datetime import date
from ai_service import generate_remarks

from database import create_table, insert_patient, view_patients, patient_exists, delete_patient, update_patient

menu = st.sidebar.selectbox("Menu",
    ["Add Patient", "View Patients", "Update Patient", "Delete Patient"])

# Create table if not exists
create_table()

# Load model
model = pickle.load(open("health_prediction_model.sav", "rb"))

st.title("🏥 Health Prediction Application")

# Patient Details
name = st.text_input("Full Name")
dob = st.date_input("Date of Birth")
email = st.text_input("Email Address")

# Blood Test Values
glucose = st.number_input("Glucose (mg/dL)", min_value=0.0)
haemoglobin = st.number_input("Haemoglobin (g/dL)", min_value=0.0)
cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0)

if st.button("Predict Disease Risk"):

    # Full Name Validation
    if not name.strip():
        st.error("Full Name is required")

    # DOB Validation
    elif dob > date.today():
        st.error("Date of Birth cannot be in the future")

    # Email Validation
    elif not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        st.error("Please enter a valid email address")

    # Blood Test Validation
    elif glucose <= 0:
        st.error("Glucose must be greater than 0")

    elif haemoglobin <= 0:
        st.error("Haemoglobin must be greater than 0")

    elif cholesterol <= 0:
        st.error("Cholesterol must be greater than 0")

    else:
    
        prediction = model.predict([[glucose, haemoglobin, cholesterol]])
        disease_risk = prediction[0]
    
        # Remarks
        remarks = generate_remarks(
        disease_risk,
        glucose,
        haemoglobin,
        cholesterol
    )
    
        st.success(f"Disease Risk: {disease_risk}")
        st.info(remarks)
    
        # Save to database only if email doesn't exist
        if patient_exists(email):
            st.warning("Patient already exists!")
    
        else:
            insert_patient(
                name,
                str(dob),
                email,
                glucose,
                haemoglobin,
                cholesterol,
                disease_risk,
                remarks
            )
    
            st.success("Patient record saved successfully!")

st.subheader("Patient Records")

if st.button("View Patients"):
    df = view_patients()
    st.dataframe(df)

if menu == "Delete Patient":

    patient_id = st.number_input("Patient ID", min_value=1, step=1)

    if st.button("Delete"):
        delete_patient(patient_id)
        st.success("Patient deleted successfully!")

if menu == "Update Patient":

    patient_id = st.number_input("Patient ID", min_value=1, step=1)

    new_remarks = st.text_area("Updated Remarks")

    if st.button("Update"):
        update_patient(patient_id, new_remarks)

        st.success("Patient updated successfully!")