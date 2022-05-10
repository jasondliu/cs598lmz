import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.CField)]

# Test ctypes.CField
class Y(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.CField)]

# Test ctypes.CField
class Z(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.CField)]

# Test ctypes.CField
class W(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.CField)]

# Test ctypes.CField
class ZZ(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.CField)]

# Test ctypes.CField
class WW(ctypes.Structure):
    _fields_ = [("x",
