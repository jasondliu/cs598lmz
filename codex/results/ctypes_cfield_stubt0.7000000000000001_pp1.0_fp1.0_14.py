import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class X(ctypes.Structure):
    pass

class Y(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]
    pass

class Z(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

if sys.version_info >= (2, 6):
    try:
        ctypes.addressof(ctypes.c_int(0))
    except TypeError:
        pass
    else:
        raise Exception("expected TypeError")

if sys.version_info < (2, 6):
    try:
        ctypes.addressof(X())
    except TypeError:
        pass
    else:
        raise Exception("expected TypeError")

if sys.version_info >= (2, 6):
    ctypes.addressof.__doc__

if sys.version_info < (2, 6):
    try:
        ctypes.pointer(ctypes.c_int(0))
    except TypeError:
        pass
    else:
