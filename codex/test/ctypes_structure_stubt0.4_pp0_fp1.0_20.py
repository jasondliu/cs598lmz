import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int

s = S()
s.x = 1

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s2 = S2(1)

class S3(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s3 = S3()
s3.x = 1

class S4(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s4 = S4()
s4.x = 1

class S5(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s5 = S5()
s5.x = 1

class S6(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

s6 = S6()
s6.x = 1
