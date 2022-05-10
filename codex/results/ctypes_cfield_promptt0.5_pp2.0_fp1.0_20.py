import ctypes
# Test ctypes.CField as a base class of ctypes.Field

class CFoo(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class CFoo2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class CField(ctypes.CField):
    def __init__(self, name, type, offset):
        self.name = name
        self.type = type
        self.offset = offset
    def __repr__(self):
        return "<CField %s>" % self.name

class CFoo3(ctypes.Structure):
    _fields_ = [CField("a", ctypes.c_int, 0)]

class CFoo4(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class CFoo5(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]

class CFoo6(ctypes.Structure):
    _fields_ = [("a",
