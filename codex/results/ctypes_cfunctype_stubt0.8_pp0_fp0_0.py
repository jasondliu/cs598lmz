import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return b"123"

cfunc = ctypes.CDLL(None).fun
cfunc.restype = ctypes.py_object
cfunc.argtypes = (ctypes.py_object, ctypes.py_object)
print(ctypes.py_object(cfunc(fun, 123)))
</code>

