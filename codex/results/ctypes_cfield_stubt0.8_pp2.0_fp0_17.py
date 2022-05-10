import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)

PyType_Type = type(S)

ctypes.PyCSimpleType_Type = type(ctypes.c_int)
ctypes.PyCArrayType_Type = type(ctypes.c_int * 4)
ctypes.PyCPointerType_Type = type(ctypes.c_int_p)
ctypes.PyCStructType_Type = type(ctypes.c_int * 4)

class C(ctypes.Structure):
    _fields_ = [('p', ctypes.POINTER(S))]

ctypes.PyCArgObject_Type = type(C())

del S, C

# XXX: The following are now defined only in the ctypes.com module
#ctypes.PyCOpaque_Type = type("opaque")
#ctypes.PyCFuncPtr_Type = type("c_functype")

#====================================================================================================================
# PyPy: test definitions
#====================================================================================================================

def test_set_pyobj():
    import ctypes
    class B(ctypes.Structure):
       
