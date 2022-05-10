import ctypes
# Test ctypes.CField
class Struct(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int),
                ('z', ctypes.c_int)]

class CFunc(ctypes.CFuncPtr):
    def __init__(self, func, restype, argtypes):
        self.restype = restype
        self.argtypes = argtypes
        self.func = func

class CStruct(ctypes.CField):
    def __init__(self, name, type, offset):
        self.name = name
        self.type = type
        self.offset = offset

class CArray(ctypes.CField):
    def __init__(self, name, type, offset, length):
        self.name = name
        self.type = type
        self.offset = offset
        self.length = length

class CUnion(ctypes.CField):
    def __init__(self, name, type, offset):
        self.name = name
        self.type = type
        self.
