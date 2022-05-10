import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(S.x)

# Without wrapping __class__ none of the following work:
# wrap(S.x.__class__)
# wrap(ctypes.CField)
# wrap(getattr(ctypes, 'CField'))
