import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

def test():
    fun_ptr = ctypes.cast(fun, ctypes.c_void_p)
    return fun_ptr.value

print(test())
