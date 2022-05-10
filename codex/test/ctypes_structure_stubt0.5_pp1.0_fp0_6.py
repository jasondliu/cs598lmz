import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int32
    y = ctypes.c_int32
    _fields_ = [("x", ctypes.c_int32),
                ("y", ctypes.c_int32)]

# test reading
s = S()
s.x = 1
s.y = 2
assert s.x == 1
assert s.y == 2

# test writing
s.x = 4
s.y = 5
assert s.x == 4
assert s.y == 5

# test accessing a field by name
s.x = 7
s.y = 8
assert s.x == 7
assert s.y == 8

# test accessing a field by index
s.x = 10
s.y = 11
assert s.x == 10
assert s.y == 11

# test accessing a field by index
s.x = 13
s.y = 14
assert s.x == 13
assert s.y == 14

# test accessing a field by index
s.x = 16
s.y = 17
assert s.x == 16
