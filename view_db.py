import sqlite3

# Connect to the database
conn = sqlite3.connect('app.db')
cursor = conn.cursor()

print("=" * 50)
print("DATABASE VIEWER")
print("=" * 50)

# Show users table
print("\n📋 USERS TABLE:")
print("-" * 30)
cursor.execute("SELECT * FROM users")
users = cursor.fetchall()

if users:
    print(f"{'ID':<3} {'Username':<15} {'Password (first 20 chars)':<25}")
    print("-" * 50)
    for user in users:
        password_preview = user[2][:20] + "..." if len(user[2]) > 20 else user[2]
        print(f"{user[0]:<3} {user[1]:<15} {password_preview:<25}")
else:
    print("No users found")

# Show todos table
print("\n📝 TODOS TABLE:")
print("-" * 30)
cursor.execute("SELECT * FROM todos")
todos = cursor.fetchall()

if todos:
    print(f"{'ID':<3} {'Title':<15} {'Description':<20} {'Completed':<10} {'Owner ID':<8}")
    print("-" * 70)
    for todo in todos:
        completed = "✅ Yes" if todo[3] else "❌ No"
        description = todo[2] if todo[2] else "No description"
        print(f"{todo[0]:<3} {todo[1]:<15} {description[:20]:<20} {completed:<10} {todo[4]:<8}")
else:
    print("No todos found")

# Show table schemas
print("\n🏗️  TABLE SCHEMAS:")
print("-" * 30)

# Users table schema
cursor.execute("PRAGMA table_info(users)")
users_schema = cursor.fetchall()
print("\nUsers table structure:")
for column in users_schema:
    print(f"  - {column[1]} ({column[2]})")

# Todos table schema
cursor.execute("PRAGMA table_info(todos)")
todos_schema = cursor.fetchall()
print("\nTodos table structure:")
for column in todos_schema:
    print(f"  - {column[1]} ({column[2]})")

conn.close()
print("\n" + "=" * 50)
print("Database file location: app.db")
print("=" * 50)

