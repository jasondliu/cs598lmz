import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect()

# test_db = 'test.sqlite3'
# if os.path.exists(test_db):
#     os.remove(test_db)
# con = sqlite3.connect(test_db)
# cur = con.cursor()
# cur.execute('CREATE TABLE test(id INTEGER, value TEXT)')
# cur.execute('INSERT INTO test VALUES(1, "test")')
# con.commit()
# cur.close()
# con.close()

# Test sqlite3.connect() using URI format

# test_db = 'test.sqlite3'
# if os.path.exists(test_db):
#     os.remove(test_db)
# con = sqlite3.connect('file:{}?mode=rwc'.format(test_db), uri=True)
# cur = con.cursor()
# cur.execute('CREATE TABLE test(id INTEGER, value TEXT)')
# cur.execute('INSERT INTO test VALUES(1, "test")')
# con.commit
