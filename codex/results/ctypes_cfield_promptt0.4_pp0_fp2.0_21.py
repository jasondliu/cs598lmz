import ctypes
# Test ctypes.CField

class X(ctypes.Structure):
    _fields_ = [("x", ctypes.CField)]

X()
X.x
X().x

class Y(ctypes.Structure):
    _fields_ = [("x", ctypes.CField)]
    def __init__(self):
        self.x = 42

Y()
Y.x
Y().x

# Test ctypes.CField subclassing

class Z(ctypes.CField):
    pass

class W(ctypes.Structure):
    _fields_ = [("x", Z)]

W()
W.x
W().x

class W(ctypes.Structure):
    _fields_ = [("x", Z)]
    def __init__(self):
        self.x = 42

W()
W.x
W().x

# Test ctypes.CField subclassing with __init__

class Z(ctypes.CField):
    def __init__(self, *args):
        pass

class W(ctypes.Structure
