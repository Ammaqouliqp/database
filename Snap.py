import sqlite3


conn = sqlite3.connect('example.db')

# Create a new table
cursor = conn.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Safir (
    safir_id INTEGER PRIMARY KEY,
    phone INTEGER,
    car_id INTEGER,
    license_id INTEGER,
    wallet_id INTEGER
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS car (
    car_id INTEGER PRIMARY KEY,
    license INTEGER
)
''')
cursor.execute('''
CREATE TABLE IF NOT EXISTS mosafer(
    mosafer_id INTEGER PRIMARY KEY,
    phone INTEGER,
    wallet_id INTEGER
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS wallet(
    wallet_id INTEGER PRIMARY KEY,
    mojodi INTEGER
)
''')



conn.commit()
conn.close()
