import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

#to create a function from the funptr, use the from_address method
#of the PyCFunctionType class

FUNPTR = ctypes.CFUNCTYPE(ctypes.py_object)
funptr = ctypes.cast(fun,FUNPTR)
f = FUNPTR.from_address(ctypes.addressof(funptr))
f()
