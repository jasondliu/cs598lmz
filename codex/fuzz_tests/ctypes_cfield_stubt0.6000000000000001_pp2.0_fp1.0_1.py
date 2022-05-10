import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class S1(S):
    _fields_ = [('y', ctypes.c_int)]

class S2(S1):
    _fields_ = [('z', ctypes.c_int)]

class S3(S2):
    _fields_ = [('t', ctypes.c_int)]

def f(s):
    print(s.x, s.y, s.z, s.t)

f(S1(1))
f(S2(1, 2))
f(S3(1, 2, 3))
</code>

