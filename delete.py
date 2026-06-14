import sqlite3

conn = sqlite3.connect("patients.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM patients")

conn.commit()
conn.close()

print("All records deleted successfully")