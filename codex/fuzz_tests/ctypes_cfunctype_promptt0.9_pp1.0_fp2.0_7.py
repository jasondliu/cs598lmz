import ctypes
# Test ctypes.CFUNCTYPE
def func_CFUNCTYPE_RETURN_VOID(int_val):
    print (int_val)
func = ctypes.CFUNCTYPE(None, ctypes.c_int)(func_CFUNCTYPE_RETURN_VOID)
func(42)

# Test ctypes.py_object
def func_py_object(obj):
    print (obj)
func = ctypes.CFUNCTYPE(ctypes.c_void_p,
                        ctypes.POINTER(ctypes.py_object))(func_py_object)
func((ctypes.py_object * 1)())

# Test exception
def func_raise_exception():
    raise Exception("test exception")
func = ctypes.CFUNCTYPE(None)(func_raise_exception)
func()
