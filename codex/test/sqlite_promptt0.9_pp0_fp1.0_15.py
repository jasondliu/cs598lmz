import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db").
import sqlite3
conn = sqlite3.connect("test.db")
cursor = conn.cursor()
# Execute EXEC SQL SELECT Name
cursor.execute("SELECT Name FROM Foods WHERE Price<=7.05")
cursor.execute("SELECT Name FROM Foods WHERE Price<=7.05")
cursor.execute("SELECT Name FROM Foods WHERE Price<=7.05")
cursor.execute("SELECT Name FROM Foods WHERE Price<=7.05")
cursor.execute("SELECT Name FROM Foods WHERE Price<=7.05")
cursor.execute("SELECT Name FROM Foods WHERE Price<=7.05")
print(cursor.fetchmany(3))
print(cursor.fetchall())

#class cdata
class cdata(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int32),
                ("b", ctypes.c_int32),
                ("c", ctypes.c_int32),
                ("d", ctypes.c_int32)]
#end

