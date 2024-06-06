import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()

cursor.execute("UPDATE users SET Safir = ?  Mosafer = ?", ("aliagha", "mamadagha"))
conn.commit()
conn.close()