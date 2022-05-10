import ctypes

class S(ctypes.Structure):
    x = ctypes.c_uint32
    y = ctypes.c_uint32

class B(ctypes.Union):
    _fields_ = [("s", S),
                ("x", ctypes.c_uint64)]

b = B()
b.s.x = 1
b.s.y = 2
b.x = 0x1122334455667788

print hex(b.s.x), hex(b.s.y)
print hex(b.x)
</code>

