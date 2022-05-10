import ctypes
# Test ctypes.CField.from_address

class A(ctypes.Structure):
    _fields_ = [("x", ctypes.c_long)]

a = A.from_address(ctypes.addressof(ctypes.c_long()))
a.x = 42
print a.x

class A(ctypes.Structure):
    _fields_ = [("x", ctypes.c_uint),
                ("y", ctypes.c_uint),
                ("z", ctypes.c_float),
                ("w", ctypes.c_float),
                ("f", ctypes.c_double),
                ]

a = A.from_address(ctypes.addressof(ctypes.c_long()))
a.x = 42
a.y = -1
a.z = 3.14
a.w = 2.718
a.f = 1.618
print repr(a.x), repr(a.y), repr(a.z), repr(a.w), repr(a.f)
print a.x, a.y, a.z, a
