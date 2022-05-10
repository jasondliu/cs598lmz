import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

def test(s):
    with s.dtor as _:
        pass
    return _

    
p = ctypes.CField('x', ctypes.c_int, 0, 0, '') 
t = test(p)
print(t)
