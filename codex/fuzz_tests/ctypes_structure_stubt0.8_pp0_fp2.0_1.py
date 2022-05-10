import ctypes

class S(ctypes.Structure):
    x = 1
    _fields_ = [("y", ctypes.c_int)]
    z = 2
    _fields_ = [("t", ctypes.c_int)]
# Make sure the type is S, not int
assert type(S.x) is S
assert S.x == 1
assert S.y == 0
assert S.z == 2
assert S.t == 0
S.x = 5
S.y = 6
S.z = 7
S.t = 8
assert S.x == 5
assert S.y == 6
assert S.z == 7
assert S.t == 8

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]
    _anonymous_ = "x"

# Make sure the type is S, not int
assert type(S2.x) is S2
assert S2.x == 0
S2.x = 3
assert S2.x == 3

class S3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int
