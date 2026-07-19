import sqlite3
from ai_query import generate_sql

def run_query(sql):
    conn = sqlite3.connect("houses.db")
    cursor = conn.cursor()
    result = cursor.execute(sql).fetchall()
    conn.close()
    return result

question = input("Ask your question: ")

sql = generate_sql(question)
print("Generated SQL:", sql)

result = run_query(sql)
print("Answer:", result)