import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int.in_dll(ctypes, 'x')
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]

assert S.x == 42
</code>
The <code>in_dll</code> mechanism was only introduced in Python 2.7 and 3.1, though.

