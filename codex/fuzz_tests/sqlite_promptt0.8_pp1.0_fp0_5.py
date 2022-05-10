import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connection()
sqlite3.dump_database('/usr/local/var/run/sensor_data.db')

# Define the mpr121 data structure
class mpr121(ctypes.Structure):
    _fields_ = [
        ("i2c_addr",      ctypes.c_uint8),
        ("thresh_touched", ctypes.c_uint8),
        ("thresh_released", ctypes.c_uint8),
        ("read_flag",     ctypes.c_uint8),
        ("debounce",      ctypes.c_uint8),
        ("last_touched_mask", ctypes.c_uint32),
        ("last_released_mask", ctypes.c_uint32),
        ("last_status",   ctypes.c_uint32),
        ("connection",    ctypes.c_void_p),
        ("mutex",         ctypes.c_void_p)
    ]

# Callback function
def callback(data, userdata):
    global last_touched, touched_mask
    if not userdata
