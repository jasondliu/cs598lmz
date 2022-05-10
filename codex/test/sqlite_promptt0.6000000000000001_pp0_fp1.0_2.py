import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("test.db")

class PyCapsule(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("pointer", ctypes.c_void_p)]

class PyCapsule_Destructor(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p),
                ("pointer", ctypes.c_void_p)]

class PyCObject(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_void_p),
                ("ob_type", ctypes.c_void_p),
                ("destructor", ctypes.c_void_p),
                ("cobject", ctypes.c_void_p)]

class py_object(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_void_p),
                ("ob_type", ctypes.c_void_p)]

