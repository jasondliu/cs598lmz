import ctypes
# Test ctypes.CField:

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
    _anonymous_ = ["x"]

print(C.x)
print(C.y)

# Test ctypes.Field:

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", ctypes.c_int)]
    _anonymous_ = ["x"]

print(C.x)
print(C.y)
