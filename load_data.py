import pandas as pd
import sqlite3

# CSV read karo
df = pd.read_csv("train_final.csv")

# DB connect
conn = sqlite3.connect("houses.db")

# Table create + data insert
df.to_sql("houses", conn, if_exists="replace", index=False)

conn.close()

print("✅ CSV data loaded into database!")