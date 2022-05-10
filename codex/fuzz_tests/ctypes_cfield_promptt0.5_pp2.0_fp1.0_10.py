import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [
        ("x", ctypes.c_int),
        ("y", ctypes.c_char),
        ("z", ctypes.c_int),
    ]

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

x = X(1, b"a", 2)

print(x.x, x.y, x.z)
print(X.x.__doc__)
print(X.y.__doc__)
print(X.z.__doc__)
