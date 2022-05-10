import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
cursor.execute("select * from test")
#result = cursor.fetchall()
#result = cursor.fetchone()
result = cursor.fetchmany(2)
print("fetch 2 result:",result)
result = cursor.fetchmany(3)
print("fetch 3 result:",result)
cursor.close()
conn.close()
print(".............................................................")

# Insert
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
#cursor.execute("insert into test values(1, ?, ?)", ('zhang', '18'))
cursor.execute("insert into test values(?, ?, ?)", (1, 'zhang', '18'))
conn.commit()
cursor.close()
conn.close()
print(".............................................................")

# Update
conn = sqlite3.connect("test.db")
