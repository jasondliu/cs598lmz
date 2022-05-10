import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    z = ctypes.c_int

class D(ctypes.Union):
    _fields_ = [("v", S), ("c", ctypes.c_char * 4)]

d = D()
d.v.z = 0x12345678
print(d.c) # '\x78\x56\x34\x12'
</code>

