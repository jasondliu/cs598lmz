import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(object):
    def __init__(self):
        self.f = S.x

print C.__dict__['f'].__class__
print type(S.x)
</code>

