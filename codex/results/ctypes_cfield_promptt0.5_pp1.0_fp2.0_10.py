import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ]
    def __init__(self, *args):
        super().__init__(*args)
        self.a = 1
        self.b = 2
        self.c = 3

# Test ctypes.CField
class C2(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
        ]
    def __init__(self, *args):
        super().__init__(*args)
        self.a = 1
        self.b = 2
        self.c = 3

# Test ctypes.CField
class C3(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c
