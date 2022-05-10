import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    def __init__(self):
        self.a = 2
X()

# Test ctypes.BigEndianStructure
class X(ctypes.BigEndianStructure):
    _fields_ = [("a", ctypes.c_int)]
    def __init__(self):
        self.a = 2
X()

# Test ctypes.LittleEndianStructure
class X(ctypes.LittleEndianStructure):
    _fields_ = [("a", ctypes.c_int)]
    def __init__(self):
        self.a = 2
X()

# Test ctypes.Union
class X(ctypes.Union):
    _fields_ = [("a", ctypes.c_int)]
    def __init__(self):
        self.a = 2
X()

# Test ctypes.CArgObject
class X(ctypes.CArgObject):
    def __init__(self, a):
        self
