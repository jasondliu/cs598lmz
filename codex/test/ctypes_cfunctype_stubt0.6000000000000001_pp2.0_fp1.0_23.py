import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

# Test that we can pass None to a CFUNCTYPE() function
fun(None)

# Test that we can pass None to a FUNTYPE() function
fun()

# Test that we can pass None to a function with a CFUNCTYPE argument
def fun2(arg):
    pass
fun2(fun)

# Test that None can be used as a callable
def fun3():
    pass
