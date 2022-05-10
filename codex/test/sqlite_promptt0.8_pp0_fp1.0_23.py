import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
db_path = "./test.db"

try:
    conn = sqlite3.connect(db_path)
except Exception as e:
    print(e)
    exit(0)

cur = conn.cursor()
sql_str = "select * from test"
try:
    cur.execute(sql_str)
except Exception as e:
    print(e)
    exit(0)

rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
