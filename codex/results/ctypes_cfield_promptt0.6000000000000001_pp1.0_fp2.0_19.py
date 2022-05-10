import ctypes
# Test ctypes.CField
class S1(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.c_int)]
s = S1()
s.a = 5
s.b = 6
print(s.a, s.b)

# Test ctypes.CField
class S2(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField)]
s = S2()
s.a = 5
s.b = 6
print(s.a, s.b)

# Test ctypes.CField
class S3(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int),
                ("b", ctypes.CField),
                ("c", ctypes.c_int)]
s = S3()
s.a = 5
s.b = 6
s.c = 7
print(s.a, s.b, s.c)

# Test ctypes.CField
class
