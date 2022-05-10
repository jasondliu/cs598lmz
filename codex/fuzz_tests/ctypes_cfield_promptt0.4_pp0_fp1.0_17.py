import ctypes
# Test ctypes.CField
class FIELD(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.CField)]

class FIELD2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.CField)]

# Test ctypes.CArray
class ARRAY(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.CArray)]

class ARRAY2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),
                ("b", ctypes.c_char),
                ("c", ctypes.CArray)]

# Test ctypes.CPointer
class POINTER(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char),

