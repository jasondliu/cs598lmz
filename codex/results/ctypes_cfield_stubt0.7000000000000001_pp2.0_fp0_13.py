import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

class Array(ctypes.Array):
    _type_ = ctypes.c_int
    _length_ = 10

ctypes.CArray = type(Array)

class Pointer(ctypes.POINTER(ctypes.c_int)):
    _type_ = ctypes.c_int

ctypes.CPointer = type(Pointer)

class Structure(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_double)]
    _pack_ = 1

ctypes.CStructure = type(Structure)

class Union(ctypes.Union):
    _fields_ = [('x', ctypes.c_int),
                ('y', ctypes.c_double)]
    _pack_ = 1

ctypes.CUnion = type(Union)

ctypes.CFunctionType = type(lambda: None)

#
# Python 2.5 don't have the following
#

if not hasattr(ctypes, 'PyCFuncPtrType'):
