import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test():
    u = {}
    getattr(S.x, '__dict__')
    S.x.__dict__
    S.x.__dict__ = u
    rais
