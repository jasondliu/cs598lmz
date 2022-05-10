import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun(): pass
typeptr = ctypes.c_size_t.from_address(id(type(fun)))
typeadr = typeptr.value
