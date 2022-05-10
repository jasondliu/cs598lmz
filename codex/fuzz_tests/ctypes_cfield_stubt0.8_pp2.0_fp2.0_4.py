import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
class O(object):
    pass

o = O()
o.x = S.x

def fn(z):
    return z.x

# crash because it doesn't check the type of the 'self' argument
fn(o)
