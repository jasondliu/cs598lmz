import ctypes
import ctypes.util
import threading
import sqlite3
import sys
import time

libXgremlin = ctypes.cdll.LoadLibrary(ctypes.util.find_library("Xgremlin"))
x_display = libXgremlin.XOpenDisplay(None)

libX11 = ctypes.cdll.LoadLibrary(ctypes.util.find_library("X11"))

def press_key(key, down):
    """Updates a key's state in the database, and uses XSendEvent to change X11's perception"""
    cursor.execute("""
                   UPDATE keys
                   SET
                       down=(?),
                       held=(?),
                       press_count=(select press_count + 1 from keys where id=(?))
                   WHERE id=(?)
                   ;""", (down, 1 if down else 0, key, key))
    db.commit()

    if down:
        event = ctypes.c_long(2)
    else:
        event = ctypes.c_long(3)

    libXgremlin.XTestFakeKeyEvent(x_display, key, down, 0)
