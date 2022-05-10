import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect with a non valid db file
try:
    con = sqlite3.connect('/tmp/doesntexist')
    print('Test 1: Error, should not be able to connect to non existing db file')
except Exception as e:
    pass
else:
    print('Test 1: Error, should not be able to connect to non existing db file')
# Test sqlite3.connect with a in memory db
con = sqlite3.connect(':memory:')
if con:
    print('Test 2: Good, we can connect to in memory db')
# Test sqlite3.connect with a valid db file
tmp_db_file = tempfile.NamedTemporaryFile()
con = sqlite3.connect(tmp_db_file.name)
if con:
    print('Test 3: Good, we can connect to a valid db file')
# Test sqlite3.connect with a valid db file
try:
    con = sqlite3.connect('/tmp/doesntexist', isolation_level=None)
    print('Test 4: Error, should not be able to connect to non existing db file')
