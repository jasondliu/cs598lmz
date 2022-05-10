import ctypes
import ctypes.util
import threading
import sqlite3

def get_lib(name):
    return ctypes.cdll.LoadLibrary(ctypes.util.find_library(name))

db = sqlite3.connect('data.db')
db.execute('''CREATE TABLE IF NOT EXISTS data(
    id INTEGER PRIMARY KEY,
    timestamp REAL NOT NULL,
    packet_length INTEGER NOT NULL,
    packet_type INTEGER NOT NULL,
    packet_direction INTEGER NOT NULL,
    packet_direction_real INTEGER NOT NULL,
    packet_address_low INTEGER NOT NULL,
    packet_address_high INTEGER NOT NULL,
    packet_data BLOB NOT NULL
)''')

c_int32 = ctypes.c_int32

class packet_st(ctypes.Structure):
    _fields_ = [
        ("timestamp", c_int32),
        ("length", c_int32),
        ("type", c_int32),
        ("direction", c_int32),
        ("direction_real", c_int32),
       
