import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/pi/Desktop/data.db')
# Test sqlite3.connect('/home/pi/Desktop/data.db').cursor().execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)')
# Test sqlite3.connect('/home/pi/Desktop/data.db').cursor().execute('INSERT INTO test (name) VALUES ("test")')
# Test sqlite3.connect('/home/pi/Desktop/data.db').cursor().execute('SELECT * FROM test')
# Test sqlite3.connect('/home/pi/Desktop/data.db').cursor().execute('SELECT * FROM test').fetchall()

# Test sqlite3.connect('/home/pi/Desktop/data.db').cursor().execute('CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, name TEXT)')
# Test sqlite3.connect('/home/pi/Desktop/data.db').cursor().execute('INSERT INTO test (name) VALUES ("test")')
# Test sqlite3
