import ctypes
# Test ctypes.CField
class K:
    _fields_ = [("i", ctypes.c_int)]
print K._fields_
print K((1,))

# Test ctypes.CField
class K:
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_double)]
print K._fields_
print K((1, 2.5))

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
print C._fields_
o = C()
o.x = 1
o.y = 4
print ctypes.c_int.from_address(ctypes.addressof(o.x))
print ctypes.c_int.from_address(ctypes.addressof(o.y))

class C(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int),
                ("y", ctypes.c_int)]
print C((1, 4))

class C(
