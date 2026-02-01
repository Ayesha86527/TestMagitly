import sqlite3

def get_user_by_email(email):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE email = '{email}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

def search_products(keyword):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products WHERE name LIKE '%%' + '" + keyword + "' + '%%'")
    products = cursor.fetchall()
    conn.close()
    return products
