**#🏥 Health Prediction Application using Machine Learning & Generative AI**

**📌 Project Overview**

The Health Prediction Application is an AI-powered healthcare solution developed using Python, Streamlit, SQLite, Machine Learning, and Gemini AI. The application allows users to manage patient records, predict potential disease risks based on blood test parameters, and generate intelligent medical remarks using Generative AI.

The system analyzes Glucose, Haemoglobin, and Cholesterol levels to predict disease risk categories such as Diabetes Risk, Heart Disease Risk, Anemia Risk, Healthy, and High Health Risk.

**🚀 Features**
✅ CRUD Operations
Add Patient Records
View Patient Records
Update Patient Remarks
Delete Patient Records
✅ Data Validation
Valid Email Validation
Date of Birth Validation
Numeric Blood Test Validation
Duplicate Patient Prevention
✅ Disease Risk Prediction

**Machine Learning model predicts:**

Healthy
Diabetes Risk
Heart Disease Risk
Anemia Risk
High Health Risk

**✅ AI-Powered Medical Remarks**

Integrated Gemini AI API
Generates intelligent health recommendations based on prediction results

**✅ Database Management**

SQLite Database
Persistent Storage of Patient Records

**🛠️ Technology Stack**

Frontend	Streamlit
Backend	Python
Database	SQLite
Machine Learning	Scikit-Learn
Algorithm	Random Forest Classifier
AI Integration	Google Gemini API
Data Processing	Pandas, NumPy

**📊 Machine Learning Workflow**

Patient Data
     │
     ▼
Data Validation
     │
     ▼
Random Forest Model
     │
     ▼
Disease Risk Prediction
     │
     ▼
Gemini AI API
     │
     ▼
AI Generated Remarks
     │
     ▼
SQLite Database
     │
     ▼
Streamlit Dashboard

**📂 Project Structure**

Health-Prediction-App/
│
├── app.py
├── database.py
├── health_prediction_model.sav
├── patients.db
├── ai_service.py
├── requirements.txt
├── README.md
└── dataset.csv
