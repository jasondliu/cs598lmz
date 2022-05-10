import ctypes
# Test ctypes.CField.
import ctypes

class Tag(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class Tag2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int),
                ("c", ctypes.c_int)]

class Tag3(ctypes.Structure):
    _fields_ = [("a", Tag),
                ("b", ctypes.c_int)]

class Tag4(ctypes.Structure):
    _fields_ = [("a", Tag),
                ("b", Tag2)]

class Tag5(ctypes.Union):
    _fields_ = [("a", Tag),
                ("b", Tag2)]

class Tag6(ctypes.Union):
    _fields_ = [("a", Tag),
                ("b", ctypes.c_int)]

class Tag7(ctypes.Structure):
    _fields_ = [("a", ctypes
