import ctypes
# Test ctypes.CField()

import ctypes

class X(ctypes.Structure):
    _fields_ = [
        ("a", ctypes.c_int),
        ("b", ctypes.c_int),
        ("c", ctypes.c_int),
    ]

class Y(ctypes.Structure):
    _fields_ = [
        ("x", X),
        ("y", ctypes.c_int),
        ("z", ctypes.c_int),
    ]


print(Y.x.offset)
print(Y.y.offset)
print(Y.z.offset)

print(ctypes.sizeof(Y))

print(ctypes.addressof(Y.x))
print(ctypes.addressof(Y.y))
print(ctypes.addressof(Y.z))

print(ctypes.addressof(Y.x.a))
print(ctypes.addressof(Y.x.b))
print(ctypes.addressof(Y.x.c))

print(ctypes.addresso
