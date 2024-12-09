import sqlite3

def get_connection():
    return sqlite3.connect("ice_cream_parlor.db")

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()
    with open("static/schema.sql", "r") as f:
        cursor.executescript(f.read())
    conn.commit()
    conn.close()
