import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A(object):
    _fields_ = [('f', ctypes.CField)]

class B(A):
    _fields_ = [('u', ctypes.c_uint)]

print(B().f)
</code>
See also Use of ctypes.Structure and .from_param() in ctypes

