import ctypes

class S(ctypes.Structure):
    x = ctypes.c_double
    y = ctypes.c_double
    z = ctypes.c_double

class C(ctypes.Structure):
    _fields_ = [("data", S)]

c = C()
c.data.x = 1.0
c.data.y = 2.0
c.data.z = 3.0

