import ctypes
# Test ctypes.CField

class PF(ctypes.Structure):
    _fields_ = [
        ("value", ctypes.c_float, 13),
    ]

    def __getattribute__(self, name):
        if name == 'value':
            return 1.0
        return ctypes.Structure.__getattribute__(self, name)

class F(ctypes.Union):
    _fields_ = [
        ("pf", PF),
        ("f", ctypes.c_float),
    ]

f = F()
f.f = 1.0
print(hex(f.pf.value))
