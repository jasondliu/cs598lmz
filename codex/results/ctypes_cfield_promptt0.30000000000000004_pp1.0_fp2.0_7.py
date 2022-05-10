import ctypes
# Test ctypes.CField
class c_field(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]

class c_field_sub(c_field):
    _fields_ = [("c", ctypes.c_int)]

class c_field_sub2(c_field_sub):
    _fields_ = [("d", ctypes.c_int)]

class c_field_sub3(c_field_sub2):
    _fields_ = [("e", ctypes.c_int)]

class c_field_sub4(c_field_sub3):
    _fields_ = [("f", ctypes.c_int)]

class c_field_sub5(c_field_sub4):
    _fields_ = [("g", ctypes.c_int)]

class c_field_sub6(c_field_sub5):
    _fields_ = [("h", ctypes.c_int)]

class c_field_sub7(c_field_sub6
