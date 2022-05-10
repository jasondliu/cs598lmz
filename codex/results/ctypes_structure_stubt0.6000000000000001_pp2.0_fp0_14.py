import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [('x', ctypes.c_int)]

class S2(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [('x', ctypes.c_int), ('z', S)]

class S3(ctypes.Structure):
    x = ctypes.c_int()
    _fields_ = [('x', ctypes.c_int), ('z', S2)]

s = S()
print s.x
s.x = 42
print s.x

s2 = S2()
print s2.x, s2.z.x
s2.x = 99
print s2.x, s2.z.x
s2.z.x = 100
print s2.x, s2.z.x

s3 = S3()
print s3.x, s3.z.x, s3.z.z.x
s3.z.z.x = 101
print s3.x, s3.z.x,
