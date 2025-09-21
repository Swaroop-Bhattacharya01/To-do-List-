import sqlite3

# Connect to the database
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

# Check what tables exist
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tables = cursor.fetchall()
print("Tables in database:", [table[0] for table in tables])

# Check users table
try:
    cursor.execute("SELECT COUNT(*) FROM users")
    user_count = cursor.fetchone()[0]
    print(f"Number of users: {user_count}")
    
    if user_count > 0:
        cursor.execute("SELECT id, username FROM users")
        users = cursor.fetchall()
        print("Users:", users)
except Exception as e:
    print("Error checking users:", e)

# Check todos table
try:
    cursor.execute("SELECT COUNT(*) FROM todos")
    todo_count = cursor.fetchone()[0]
    print(f"Number of todos: {todo_count}")
    
    if todo_count > 0:
        cursor.execute("SELECT id, title, completed, owner_id FROM todos")
        todos = cursor.fetchall()
        print("Todos:", todos)
except Exception as e:
    print("Error checking todos:", e)

conn.close()
