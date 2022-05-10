import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
print(S.x.__class__.__mro__)
print(S.x.__class__.__mro__ == (
    <class 'ctypes._CField'>,
    <class 'ctypes.Field'>,
    <class 'object'>
))

# (Pdb) S.x.__class__
# <class 'ctypes._CField'>
# (Pdb) S.x.__class__.__mro__
# (<class 'ctypes._CField'>, <class 'ctypes.Field'>, <class 'object'>)
