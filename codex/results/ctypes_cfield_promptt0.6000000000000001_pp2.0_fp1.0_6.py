import ctypes
# Test ctypes.CField instance

class X(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int)]

X._fields_[0].__dict__

X()
