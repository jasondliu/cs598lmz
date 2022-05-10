import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    y = ctypes.c_int
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s = S()
s.x = 1
s.y = 2
print s.x, s.y

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]

s2 = S2()
s2.x = 1
s2.y = 2
print s2.x, s2.y

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    x = 1
    y = 2

s3 = S3()
print s3.x, s3.y

class S4(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int), ('y', ctypes.c_int)]
    def __init__
