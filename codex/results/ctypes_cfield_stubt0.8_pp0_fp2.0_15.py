import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class D(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char_p)]
ctypes.CArray = type(D.x)

dll = ctypes.CDLL(find_library('c'))

try:
    ctypes.c_ssize_t
except AttributeError:
    pass
else:
    class G(ctypes.Structure):
        _fields_ = [('x', ctypes.c_ssize_t)]
    ctypes.CArray = type(G.x)

class A(ctypes.Structure):
    _fields_ = [('x', ctypes.c_char * 5)]

if hasattr(ctypes, 'c_longlong'):
    class B(ctypes.Structure):
        _fields_ = [('x', ctypes.c_longlong)]

if hasattr(ctypes, 'c_ulonglong'):
    class H(ctypes.Structure):
        _fields_ = [('x', ctypes.c_ulonglong)]

