import ctypes
# Test ctypes.CField subclass
class S(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                (1, ctypes.c_int)]

class CField(ctypes.CField):
    def __init__(self, field_descriptor):
        self.offset = field_descriptor[2]
        self.bits = 0
        self.size = 1
        self.name = "1"

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                (CField((1, 1, 1)), ctypes.c_int)]

class C(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int),
                (1, ctypes.c_int)]

class C(ctypes.Union):
    _fields_ = [('a', ctypes.c_int),
                (1, ctypes.c_int)]

class D(ctypes.Structure):
    _fields_ = [('a', ctypes.c_
