import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.CDLL):
    pass

class F(ctypes.Function):
    pass

C.c_f = F((ctypes.CField * 5)(), ctypes.c_int, C)

C.c_f.restype = ctypes.c_int
C.c_f.argtypes = (ctypes.CField * 5,)

print(C.c_f([1, 2, 3, 4, 5]))
</code>
Output:
<code>$ python3 a.py
15
</code>
Yes, this is really ugly.

