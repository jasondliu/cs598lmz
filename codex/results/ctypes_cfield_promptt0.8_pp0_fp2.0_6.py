import ctypes
# Test ctypes.CField

import _ctypes_test

if _ctypes_test.makesym('union1') is not None:

    class X(ctypes.Structure):
        _fields_ = [("a", ctypes.c_int),
                    ("b", ctypes.c_int)]

    class Y(ctypes.Union):
        _fields_ = [("x", _ctypes_test.makesym('union1')),
                    ("y", _ctypes_test.makesym('union2'))]

    y = Y()
    x = X()
    import pdb; pdb.set_trace()
    x.a = 1
    y.x = x
    x.b = 2
    x.a = 3
    y.y = x
    if y.x.a != 3:
        raise RuntimeError, 'inconsistent'
