import ctypes
# Test ctypes.CField
class test_field(ctypes.Structure):
    _fields_ = [("x", ctypes.c_void_p)]

class test_int(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class test_shrt(ctypes.Structure):
    _fields_ = [("a", ctypes.c_short)]

class test_byt(ctypes.Structure):
    _fields_ = [("a", ctypes.c_byte)]

class test_chr(ctypes.Structure):
    _fields_ = [("a", ctypes.c_char)]

class test_bool(ctypes.Structure):
    _fields_ = [("a", ctypes.c_bool)]

class test_long(ctypes.Structure):
    _fields_ = [("a", ctypes.c_long)]

class test_ulong(ctypes.Structure):
    _fields_ = [("a", ctypes.c_ulong)]

class test_longlong(ctypes
