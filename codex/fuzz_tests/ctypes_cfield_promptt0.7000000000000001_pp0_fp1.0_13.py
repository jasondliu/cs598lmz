import ctypes
# Test ctypes.CField to create a union.

class CTest(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_uint),
        ('b', ctypes.CField, 0, ctypes.c_float),
        ('c', ctypes.CField, 0, ctypes.c_double),
        ('d', ctypes.c_long)
    ]

print CTest.b.offset, CTest.b.size
print CTest.c.offset, CTest.c.size
print CTest.d.offset, CTest.d.size
