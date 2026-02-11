import sqlite3

# 1. Connect to SQLite database (it will create if not exists)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# 2. Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
""")

# 3. Insert data (Parameterized Query)
def insert_user(name, age, email):
    cursor.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?)",
                   (name, age, email))
    conn.commit()
    print("User inserted successfully.")

# 4. Fetch data
def fetch_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("\n--- User Records ---")
    for row in rows:
        print(row)

# 5. Update user
def update_user(user_id, new_age):
    cursor.execute("UPDATE users SET age = ? WHERE id = ?",
                   (new_age, user_id))
    conn.commit()
    print("User updated successfully.")

# 6. Delete user
def delete_user(user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print("User deleted successfully.")

# -------- Testing --------

insert_user("Praveen", 23, "praveen@gmail.com")
insert_user("Ravi", 25, "ravi@gmail.com")

fetch_users()

update_user(1, 24)
fetch_users()

delete_user(2)
fetch_users()

# 7. Close connection
conn.close()
