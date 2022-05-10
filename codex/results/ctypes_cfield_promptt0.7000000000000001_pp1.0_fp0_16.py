import ctypes
# Test ctypes.CField
class C(ctypes.Structure):
    _fields_ = [("a", ctypes.c_ushort),
                ("b", ctypes.c_ushort),
                ("c", ctypes.CField)]
    def __init__(self):
        self.c = self.a * 10 + self.b
try:
    ctypes.CField
except AttributeError:
    print("SKIP")
    raise SystemExit

x = C()
print(x.c)

x.a = 20
x.b = 30
print(x.c)

x.c = 300
print(x.a, x.b, x.c)

# Test ctypes.CField in a nested Structure
class C2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_ushort),
                ("b", ctypes.c_ushort),
                ("c", ctypes.CField)]
    def __init__(self):
        self.c = self.a * 10 + self.b

class D(ctypes
