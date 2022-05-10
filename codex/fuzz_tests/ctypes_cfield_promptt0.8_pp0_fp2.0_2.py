import ctypes
# Test ctypes.CField
class Bar(ctypes.Structure):
    _fields_ = [("boo", ctypes.CField)]

b = Bar.from_buffer(ctypes.c_uint(0x1234)) # causes segfault
print(b.boo)
