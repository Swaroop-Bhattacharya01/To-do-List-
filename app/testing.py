import psycopg2

try:
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="Roopu@183381",
        host="thouejhmxebjqqjetosd.supabase.co",
        port="5432"
    )
    print("Connection successful!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)