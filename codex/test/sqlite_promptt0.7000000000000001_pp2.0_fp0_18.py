import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/var/log/pulse/asound.state.db").execute("SELECT * FROM card_profiles").fetchall()
# Test sqlite3.connect("/var/log/pulse/asound.state.db").execute("SELECT * FROM cards").fetchall()

class _CARD(ctypes.Structure):
    _fields_ = [
            ("name", ctypes.c_ubyte * 32),
            ("longname", ctypes.c_ubyte * 80),
            ("driver", ctypes.c_ubyte * 32),
            ("owner_module", ctypes.c_uint),
            ("flags", ctypes.c_uint),
            ("profiles", ctypes.c_void_p),
            ("active_profile", ctypes.c_void_p),
            ("n_profiles", ctypes.c_uint),
            ("proplist", ctypes.c_void_p)
            ]

