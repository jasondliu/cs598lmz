import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return b"Hello World!"

# get the address of the function
addr = ctypes.cast(fun, ctypes.c_void_p).value
# use the address as the function pointer
ptr = ctypes.cast(addr, FUNTYPE)
# call the function
print(ptr())
