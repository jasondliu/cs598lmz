import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(UserClass):
    field = ctypes.CField()

class Y(UserClass):
    field = ctypes.CField(getter=lambda s: s.__dict__['field'])

class Z(UserClass):
    field = ctypes.CField(setter=lambda s,v: s.__dict__.__setitem__('field', v))

S = ctypes.c_int

class T(UserClass):
    field = S()

class U(UserClass):
    field = S(getter=lambda s: s.__dict__['field'])

class V(UserClass):
    field = S(setter=lambda s,v: s.__dict__.__setitem__('field', v))

class W(UserClass):
    field = S(getter=lambda s: s.__dict__['field'],
              setter=lambda s,v: s.__dict__.__setitem__('field', v))

# Note: when we say 'UserClass' we really mean 'object', because
