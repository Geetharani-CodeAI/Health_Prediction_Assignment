import sqlite3
import pandas as pd

conn = sqlite3.connect("patients.db")

df = pd.read_sql_query(
    "SELECT * FROM patients",
    conn
)

print(df)

conn.close()