import sqlite3

conn = sqlite3.connect("houses.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS houses (
    id INTEGER PRIMARY KEY,
    location TEXT,
    price INTEGER,
    sqft INTEGER,
    bedrooms INTEGER
)
""")

# sample data
data = [
    ("Mohali", 5000000, 1200, 3),
    ("Chandigarh", 9000000, 1800, 4),
    ("Delhi", 15000000, 2200, 5)
]

cursor.executemany("INSERT INTO houses (location, price, sqft, bedrooms) VALUES (?, ?, ?, ?)", data)

conn.commit()
conn.close()

print("Database ready!")