import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('db.sqlite3')

#global init
#global clear

class LibOpenVG(object):
    def __init__(self):
        try:
            lib_path = ctypes.util.find_library('OpenVG')
        except Exception as e:
            print('Exception: '+str(e))
        else:
            if lib_path is None:
                raise ValueError('OpenVG library not found')

            self.lib = ctypes.cdll.LoadLibrary(lib_path)
            self.lib.vgSetfv.restype = None

        self.lib.vgSetParameteri.restype = None
        self.lib.vgGetParameterfv.restype = None
        self.lib.vgCreatePath.restype = ctypes.c_uint32
        self.lib.vgGetError.restype = ctypes.c_uint32

        self.lib.vgSetf.restype = None
        self.lib.vgGetf.restype = None
        self.lib.vgDrawPath.restype = None

