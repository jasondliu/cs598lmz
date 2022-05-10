import ctypes
# Test ctypes.CField_Type.from_address()

class X(ctypes.Structure):
    _fields_ = [
        ('a', ctypes.c_int),
        ('b', ctypes.c_int),
        ('c', ctypes.c_int),
        ('d', ctypes.c_int),
    ]

x = X()

# address of x.a
address = ctypes.addressof(x) + ctypes.sizeof(ctypes.c_int)

# address of x.b
address += ctypes.sizeof(ctypes.c_int)

# address of x.c
address += ctypes.sizeof(ctypes.c_int)

# address of x.d
address += ctypes.sizeof(ctypes.c_int)

# make sure the address is correct
assert ctypes.addressof(x.d) == address

# make sure from_address() can find the correct field
assert ctypes.CField_Type.from_address(address).name == 'd'

# make sure from_address()
