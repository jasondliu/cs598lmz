import ctypes
# Test ctypes.CField
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT(1, 2)
print(p.x)
print(p.y)

# Test ctypes.CField.from_address
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT.from_address(id(p))
print(p.x)
print(p.y)

# Test ctypes.CField.from_buffer
class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]

p = POINT.from_buffer(b"\x00\x00\x00\x00\x00\x00\x00\x00")
print(p.x)
print(p.y)

# Test
