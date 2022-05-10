import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
s.x = 42
print(s.x)
s.y = 43
print(s.y)

s = S2()
s.x = 42
print(s.x)
s.y = 43
print(s.y)

# test that ctypes.CField is a subclass of ctypes.c_int
assert issubclass(ctypes.CField, ctypes.c_int)

# test that ctypes.CField is not a subclass of ctypes.c_long
assert not issubclass(ctypes.CField, ctypes.c_long)
