import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.CField)]

ctypes.CStructure = type(C)

class S2(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField2 = type(S2.x)

class C2(ctypes.Structure):
    _fields_ = [('x', ctypes.CField2)]

ctypes.CStructure2 = type(C2)

ctypes.CArray = ctypes.c_int * 4
ctypes.CPointer = ctypes.POINTER(ctypes.c_int)

ctypes.CFunctionType = ctypes.CFUNCTYPE(ctypes.c_int)

ctypes.CString = ctypes.c_char_p

ctypes.CStringArray = ctypes.POINTER(ctypes.c_char_p)

ctypes.CBytes = ctypes.c_char * 4

ctypes.CBytesArray
