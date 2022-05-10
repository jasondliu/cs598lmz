import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/lg/.mozilla/firefox/kpvfq7z1.default/places.sqlite")

class win32_structures:
    class RECT(ctypes.Structure):
        _fields_ = [("left", ctypes.c_long),
                    ("top", ctypes.c_long),
                    ("right", ctypes.c_long),
                    ("bottom", ctypes.c_long)]
        
    class GUITHREADINFO(ctypes.Structure):
        _fields_ = [("cbSize", ctypes.c_ulong),
                    ("flags", ctypes.c_ulong),
                    ("hwndActive", ctypes.c_ulong),
                    ("hwndFocus", ctypes.c_ulong),
                    ("hwndCapture", ctypes.c_ulong),
                    ("hwndMenuOwner", ctypes.c_ulong),
                    ("hwndMoveSize", ctypes.c_ulong),
                    ("hwndCaret", ctypes.c_ulong),
                    ("rcCaret", RECT)]

