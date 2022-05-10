import ctypes
import ctypes.util
import threading
import sqlite3

class XScreensaverInfo ( ctypes.Structure ):
    _fields_ = [
        ('window', ctypes.c_ulong), # screen saver window
        ('state', ctypes.c_int), # off,on,disabled
        ('kind', ctypes.c_int), # blanked,internal,external
        ('since', ctypes.c_ulong), # milliseconds
        ('idle', ctypes.c_ulong), # milliseconds
        ('event_mask', ctypes.c_ulong) # events
        ]

class Screensaver(threading.Thread):
    def __init__(self):
        self.display = None
        self.xidle = None
        threading.Thread.__init__(self)

    def init(self):
        self.display = ctypes.CDLL(ctypes.util.find_library('X11'))
        self.display.XOpenDisplay.argtypes = [ ctypes.c_char_p ]
        self.display.XOpenDisplay.restype = ctypes.c_void_p


