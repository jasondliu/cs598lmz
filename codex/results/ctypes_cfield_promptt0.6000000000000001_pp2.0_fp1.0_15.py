import ctypes
# Test ctypes.CField
class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int, 1)]

s = S()
s.x = 1
s.y = -1
assert s.x == 1
assert s.y == 1

s.x = -1
s.y = 1
assert s.x == -1
assert s.y == -1

s.x = 0
s.y = 0
assert s.x == 0
assert s.y == 0

# Test ctypes.CField.from_param
class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_int, 1)]

s = S()
s.x = 1
s.y = 1
assert s.x == 1
assert s.y == 1

s.x = -1
s.y = -1
assert s.x == -1
assert s.y == -1

s.x = 0

