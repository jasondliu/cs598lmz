import ctypes
# Test ctypes.CField

# This field should be ignored
class S(ctypes.Structure):
    pass
S._fields_ = [("x", ctypes.c_int)]

class S1(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int)]

class S2(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", S1)]

class S3(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", S1),
                ("z", ctypes.CField)]

class S4(ctypes.Structure):
    _fields_ = [("x", ctypes.c_int), ("y", S1),
                ("z", ctypes.CField)]
    class _anonymous_:
        _fields_ = [("a", ctypes.c_int), ("b", ctypes.c_int)]

s = S()
s.x = 5
print(s.x)

s1 = S1()
