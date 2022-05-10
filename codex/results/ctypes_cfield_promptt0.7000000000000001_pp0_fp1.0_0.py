import ctypes
# Test ctypes.CField.
import _ctypes_test

class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_long),
                ("b", ctypes.c_long),
                ("c", ctypes.c_long),
                ("d", ctypes.c_long),
                ("e", ctypes.c_long),
                ("f", ctypes.c_long),
                ("g", ctypes.c_long),
                ("h", ctypes.c_long),
                ("i", ctypes.c_long),
                ("j", ctypes.c_long),
                ("k", ctypes.c_long),
                ("l", ctypes.c_long),
                ("m", ctypes.c_long),
                ("n", ctypes.c_long),
                ("o", ctypes.c_long),
                ("p", ctypes.c_long),
                ("q", ctypes.c_long),
                ("r", ctypes.c_long),
                ("s", ctypes.c_long),
                ("t
