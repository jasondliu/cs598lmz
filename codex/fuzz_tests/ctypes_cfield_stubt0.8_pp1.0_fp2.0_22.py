import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
ctypes.CStructure = type(S)
ctypes.Union = type(ctypes.Union())
ctypes.PUnion = type(ctypes.POINTER(ctypes.Union))
ctypes.CSimple = type(ctypes.c_int)
ctypes.CPointer = type(ctypes.pointer(ctypes.c_int()))
ctypes.CArray = type(ctypes.c_int*1)
ctypes.PArray = type(ctypes.POINTER(ctypes.c_int*1))
ctypes.CFuncPtr = type(ctypes.CFUNCTYPE(ctypes.c_int))
ctypes.CString = type(ctypes.c_char_p)
ctypes.PString = type(ctypes.POINTER(ctypes.c_char_p))
ctypes.Py_ssize_t = ctypes.c_int

if sys.byteorder == "little":
    ctypes._endian = "<"
else:
    ctypes._endian = ">"

def _CData_get_
