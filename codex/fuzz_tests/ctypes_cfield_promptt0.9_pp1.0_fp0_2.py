import ctypes
# Test ctypes.CField
# This variable is not usable, it's only a description.
class X(ctypes.Structure):
    _fields_ = [("m", ctypes.c_int)]
    if os.sys.platform == 'win32':
        _pack_ = 4

class XX(X):
    _fields_ = [("a", ctypes.c_char_p)]

class Y(ctypes.Structure):
    _fields_ = [("n", ctypes.c_int)]
    if os.sys.platform == 'win32':
        _pack_ = 4

class Z(ctypes.Structure):
    if os.sys.platform == 'win32':
        _pack_ = 4
    _fields_ = [("o", ctypes.c_int)]

class XY(Y, X):
    if os.sys.platform == 'win32':
        _pack_ = 4
    _fields_ = [("p", ctypes.c_int),
                ("q", ctypes.c_int),
                X("r"),
                Y("s"),
                ("
