import ctypes
# Test ctypes.CField()

class S(ctypes.Structure):
    _fields_ = [("f", ctypes.CField)]

class X(ctypes.Structure):
    _fields_ = [("s", S)]

x = X()
x.s.f = "hello"
print x.s.f
