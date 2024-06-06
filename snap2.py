import sqlite3
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Insert a single user
cursor.execute("INSERT INTO users (Mosafer, Safir) VALUES (?, ?)", ("mamadagha", "aliagha"))


cursor.execute("INSERT INTO Prices (Mosafer, Safir) VALUES (?, ?)", ("mamadagha", "aliagha"))

# Insert multiple users
users = [("mamad", "ali"), ("karim", "benzema"), ("David", "Ramos")]
cursor.executemany("INSERT INTO users (Mosafer, Safir) VALUES (?, ?)", users)

conn.commit()
conn.close()