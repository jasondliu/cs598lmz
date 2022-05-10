import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class C(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CStructure = type(C)

class X(object):
    pass

class Y(object):
    pass

ctypes.CArray = type([])
ctypes.CPointer = type(ctypes.pointer(ctypes.c_int()))
ctypes.CFunctionType = type(ctypes.CFUNCTYPE(ctypes.c_int))

# XXX find something better than X and Y
ctypes.CString = type(ctypes.c_char_p(""))
ctypes.CStringArray = type(ctypes.c_char_p("", X))
ctypes.CBytes = type(ctypes.c_char(""))
ctypes.CBytesArray = type(ctypes.c_char("", X))

ctypes.CArrayPointer = type(ctypes.c_char_p("", Y))
ctypes.CPointerPointer = type(ctypes.pointer(ctypes.pointer
