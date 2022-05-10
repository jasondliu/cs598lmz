import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/home/pi/Desktop/test.db')
# Test sqlite3.connect('/home/pi/Desktop/test.db').cursor().execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY, data TEXT)")
# Test sqlite3.connect('/home/pi/Desktop/test.db').cursor().execute("INSERT INTO test(data) VALUES (?)", (data,))
# Test sqlite3.connect('/home/pi/Desktop/test.db').cursor().execute("SELECT * FROM test").fetchall()
# Test sqlite3.connect('/home/pi/Desktop/test.db').cursor().execute("DROP TABLE test")

# Test https://github.com/adafruit/Adafruit_Python_GPIO/blob/master/Adafruit_GPIO/SPI.py
# Test https://github.com/adafruit/Adafruit_Python_GPIO/blob/master/Adafruit_GPIO/Platform.py
# Test https://github.com/adafruit/Ad
