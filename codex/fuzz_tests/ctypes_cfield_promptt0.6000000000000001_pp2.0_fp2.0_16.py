import ctypes
# Test ctypes.CField

class S(ctypes.Structure):
    _fields_ = [("value", ctypes.c_int)]
    _pack_ = 1

class C(ctypes.Structure):
    _fields_ = [("s", S)]
    _pack_ = 1

class D(ctypes.Structure):
    _fields_ = [("c", C)]
    _pack_ = 1

class E(ctypes.Structure):
    _fields_ = [("s", S)]
    _pack_ = 1

class F(ctypes.Structure):
    _fields_ = [("d", D),
                ("e", E)]
    _pack_ = 1

o = F()
print o.d.c.s.value
o.d.c.s.value = 42
print o.e.s.value
