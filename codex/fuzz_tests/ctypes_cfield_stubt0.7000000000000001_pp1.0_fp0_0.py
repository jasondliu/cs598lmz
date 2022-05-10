import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

try:
    ctypes.CField.foo
except AttributeError:
    print('AttributeError')
</code>

