import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [("f", ctypes.c_int)]

    class C(ctypes.Structure):
        _fields_ = [(ctypes.CField("a"), ctypes.POINTER(S))]

class C_Union(ctypes.Union):
    _fields_ = [(ctypes.CField("a"), ctypes.POINTER(S))]

class C_Array(ctypes.Structure):
    _fields_ = [(ctypes.CField("a"), S * 1)]

class C_Pointer(ctypes.Structure):
    _fields_ = [(ctypes.CField("a"), ctypes.POINTER(S))]

# Check the _length_ field is automatically added when a CField is used
# in a Structure or Union
class D_Union(ctypes.Union):
    _fields_ = [("a", ctypes.c_int),
                (ctypes.CField("b"), S * 1)]

class D_Structure(ctypes.Structure):
    _fields_
