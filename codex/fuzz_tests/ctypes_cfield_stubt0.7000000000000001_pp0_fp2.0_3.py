import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class A:
    def __init__(self):
        self.f = ctypes.c_int()

print(isinstance(A.f, ctypes.CField))
</code>

