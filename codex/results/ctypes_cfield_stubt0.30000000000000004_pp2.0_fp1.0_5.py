import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C:
    pass

ctypes.CField.__set__(C, 42)
</code>
This raises <code>TypeError: descriptor '__set__' for 'CField' objects doesn't apply to a 'C' object</code>.

