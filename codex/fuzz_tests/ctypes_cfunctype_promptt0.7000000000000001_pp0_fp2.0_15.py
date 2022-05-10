import ctypes
# Test ctypes.CFUNCTYPE
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    def __init__(self):
        self.a = 1

def f(x):
    print x.a
    return ctypes.pointer(X())

F = ctypes.CFUNCTYPE(ctypes.POINTER(X), ctypes.POINTER(X))
g = F(f)
print g(None).contents.a
g(None).contents.a = 2
print g(None).contents.a

# Test ctypes.Structure
class Y(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
    def __init__(self):
        self.a = 1

x = Y()
print x.a
x.a = 2
print x.a

try:
    class Z(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int)]
        def __init__(self):
            self.a = 1
