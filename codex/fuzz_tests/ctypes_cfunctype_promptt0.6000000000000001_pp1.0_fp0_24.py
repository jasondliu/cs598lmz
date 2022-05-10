import ctypes
# Test ctypes.CFUNCTYPE(restype, *argtypes)

if os.name == "nt":
    import _ctypes_test
    dll = ctypes.CDLL(_ctypes_test.__file__)
    func = dll._testfunc_p_p
else:
    func = ctypes.CDLL(None).strdup

CMPFUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)

@CMPFUNC
def compare(s1, s2):
    print("compare", s1, s2)
    return ctypes.cast(s1, ctypes.c_void_p).value - ctypes.cast(s2, ctypes.c_void_p).value

class X(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char_p)]

class Y(X):
    _fields_ = [("bla", ctypes.c_int)]

if os.name == "nt":
   
