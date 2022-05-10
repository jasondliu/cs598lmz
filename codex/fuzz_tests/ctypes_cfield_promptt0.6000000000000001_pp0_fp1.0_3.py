import ctypes
# Test ctypes.CField.

class C(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int, 2),
        ('c', ctypes.c_int, 2),
        ('d', ctypes.c_int, 2),
        ('e', ctypes.c_int, 2),
    ]

c = C()
print(ctypes.sizeof(c))

c = C.from_buffer(bytearray(ctypes.sizeof(c)))
print(ctypes.sizeof(c))

c = C.from_buffer_copy(bytearray(ctypes.sizeof(c)))
print(ctypes.sizeof(c))
