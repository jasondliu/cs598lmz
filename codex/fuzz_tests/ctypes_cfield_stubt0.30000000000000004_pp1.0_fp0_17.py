import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class CFuncPtr(ctypes.CFuncPtr):
    _flags_ = ctypes.FUNCFLAG_CDECL

class CArray(ctypes.CArray):
    _type_ = ctypes.c_int

class CString(ctypes.CString):
    pass

class POINTER(ctypes.POINTER):
    _type_ = ctypes.c_int

class Structure(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

class Union(ctypes.Union):
    _fields_ = [('x', ctypes.c_int)]

class _SimpleCData(ctypes.SimpleType):
    _type_ = 'i'
    _length_ = 1

class _SimpleCData_p(ctypes.SimpleType):
    _type_ = 'P'
    _length_ = 1

class _SimpleCData_pp(ctypes.SimpleType):
    _type_ = 'P'
    _length_ = 2

class _SimpleCData_ppp(ctypes
