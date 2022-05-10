import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CStruct = type(S)
ctypes.CArray = type((ctypes.c_int * 10)())
ctypes.CPointer = type(ctypes.pointer(ctypes.c_int()))
ctypes.CString = type(ctypes.c_char_p())
ctypes.CFunc = type(ctypes.CFUNCTYPE(ctypes.c_int))

del S
