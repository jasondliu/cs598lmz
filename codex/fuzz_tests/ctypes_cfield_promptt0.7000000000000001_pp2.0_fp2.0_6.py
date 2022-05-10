import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    def __init__(self):
        self.y = ctypes.CField(ctypes.c_int, "y")
    def __setattr__(self, attr, val):
        if attr == "y":
            self.y = val
        else:
            ctypes.Structure.__setattr__(self, attr, val)

x = X()
x.y = 15
print x.y
x.y = 100
print x.y

# Test ctypes.CField with overridden _fields_
class Y(ctypes.Structure):
    _fields_ = [("y", ctypes.c_int)]
    def __init__(self):
        self.y = ctypes.CField(ctypes.c_int, "y")
    def __setattr__(self, attr, val):
        if attr == "y":
            self.y = val
        else:
            ctypes.Structure.__setattr__(self, attr, val)

y =
