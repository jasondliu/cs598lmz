import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.CField)]

# Test ctypes.CFieldArray
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.CField * 3)]
