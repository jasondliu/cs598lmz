import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
# CONN = sqlite3.connect('test.db')
# CURSOR = CONN.cursor()
# CURSOR.execute('CREATE TABLE person (id INTEGER PRIMARY KEY, name STRING, addr STRING)')
# CURSOR.execute("INSERT INTO person (name, addr) VALUES ('Mike', 'China')")
# CURSOR.execute("INSERT INTO person (name, addr) VALUES ('Nancy', 'USA')")
# CURSOR.execute("INSERT INTO person (name, addr) VALUES ('Jun', 'Japan')")
# CURSOR.execute("INSERT INTO person (name, addr) VALUES ('DD', 'USA')")
# CURSOR.execute("INSERT INTO person (name, addr) VALUES ('JJ', 'Japan')")
# CONN.commit()
# CURSOR.execute('SELECT * from person')
# for row in CURSOR:
#     print(row)
# CURSOR.close()
# CONN.close()

# Test c
