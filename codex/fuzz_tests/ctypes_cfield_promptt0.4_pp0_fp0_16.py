import ctypes
# Test ctypes.CField
class CTest(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
    ]
    _anonymous_ = ('b',)

ct = CTest(1, 2, 3)
print(ct.a, ct.b, ct.c)

# Test ctypes.CField.from_address
ctypes.c_int.from_address(ctypes.addressof(ct.a)).value = 4
print(ct.a, ct.b, ct.c)

# Test ctypes.CField.from_buffer
ctypes.c_int.from_buffer(ct, ctypes.sizeof(ctypes.c_int)).value = 5
print(ct.a, ct.b, ct.c)

# Test ctypes.CField.from_buffer_copy
ctypes.c_int.from_buffer_copy(ct, ctypes.sizeof(ctypes.c_
