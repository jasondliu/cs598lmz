import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()
test_db = "test.sqlite3"
test_table = "test"
test_value = "THIS IS A TEST VALUE"
conn = sqlite3.connect(test_db)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE %s (dict text)''' % (test_table))
cursor.execute('''delete from %s''' % (test_table))
cursor.execute('''INSERT INTO %s (dict) VALUES ("%s")''' % (test_table, test_value))
row = cursor.execute('''SELECT dict FROM %s''' % (test_table)).fetchone()
conn.commit()
