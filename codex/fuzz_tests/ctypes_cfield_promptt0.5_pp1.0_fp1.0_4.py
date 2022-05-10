import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [
        ("_a", ctypes.c_int),
        ("_b", ctypes.c_int),
    ]

    a = ctypes.CField("_a")
    b = ctypes.CField("_b")

    def __init__(self):
        self.a = 1
        self.b = 2

c = C()
print c.a, c.b
c.a = 3
c.b = 4
print c.a, c.b
# Test ctypes.CField with a CArray
class C(ctypes.Structure):
    _fields_ = [
        ("_a", ctypes.c_int),
        ("_b", ctypes.c_int),
        ("_c", ctypes.c_int*2),
    ]

    a = ctypes.CField("_a")
    b = ctypes.CField("_b")
    c = ctypes.CField("_c")

    def __init__(self):
        self.
