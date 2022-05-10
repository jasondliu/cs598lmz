import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(C)

class D(C):
    _fields_ = [('y', ctypes.c_int)]

ctypes.CUnion = type(ctypes.Union)
ctypes.CArray = type(ctypes.c_int * 1)
ctypes.CPointer = type(ctypes.POINTER(ctypes.c_int))
ctypes.CString = type(ctypes.c_char_p)
ctypes.CFunction = type(ctypes.CFUNCTYPE(ctypes.c_int))

# On Windows, ctypes is a DLL, so the type of the ctypes module is
# a CDLL.  On other platforms it's a regular module, so the type of
# the ctypes module is a module.  This is useful for detecting
# whether the platform is Windows (if so, the value of
# ctypes.__name__ is '_ctypes').

ctypes.
