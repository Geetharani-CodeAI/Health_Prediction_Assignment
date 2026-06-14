import sqlite3
import pandas as pd

def create_table():

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name TEXT NOT NULL,
        dob TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        glucose REAL NOT NULL,
        haemoglobin REAL NOT NULL,
        cholesterol REAL NOT NULL,
        disease_risk TEXT,
        remarks TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_patient(full_name, dob, email,
                   glucose, haemoglobin, cholesterol,
                   disease_risk, remarks):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO patients
    (full_name,dob,email,glucose,haemoglobin,cholesterol,disease_risk,remarks)
    VALUES (?,?,?,?,?,?,?,?)
    """,
    (
        full_name,
        dob,
        email,
        glucose,
        haemoglobin,
        cholesterol,
        disease_risk,
        remarks
    ))

    conn.commit()
    conn.close()


def patient_exists(email):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM patients WHERE email=?",
        (email,)  )

    result = cursor.fetchone()

    conn.close()

    return result


def view_patients():

    conn = sqlite3.connect("patients.db")

    df = pd.read_sql_query("SELECT * FROM patients", conn)

    conn.close()

    return df

def update_patient(patient_id, remarks):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE patients
    SET remarks = ?
    WHERE id = ?
    """, (remarks, patient_id))

    conn.commit()
    conn.close()


def delete_patient(patient_id):

    conn = sqlite3.connect("patients.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM patients WHERE id=?",
        (patient_id,))

    conn.commit()
    conn.close()