from database import get_connection

def add_flavor(name, is_seasonal, allergens):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO flavors (name, is_seasonal, allergens) VALUES (?, ?, ?)", 
                   (name, is_seasonal, allergens))
    conn.commit()
    conn.close()

def search_flavors(search_query):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM flavors WHERE name LIKE ?", (f"%{search_query}%",))
    results = cursor.fetchall()
    conn.close()
    return results
