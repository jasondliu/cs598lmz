import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int

s = S()
print(s.x)
s.x = 0x1234
print(s.x)
s.y = 0x5678
print(s.y)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s2 = S2()
print(s2.x)
s2.x = 0x1234
print(s2.x)
s2.y = 0x5678
print(s2.y)

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int), ('z', ctypes.c_int)]

s3 = S3()
print(s3.x)
s3.x = 0x1234
print(s3.x)
s3.y = 0x5678
print(s3.y)
s
