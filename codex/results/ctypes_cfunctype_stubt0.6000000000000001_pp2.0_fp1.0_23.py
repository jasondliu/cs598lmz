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
None(fun3)

# Test that None can be called with *args and **kwds
def fun4(arg):
    pass
None(*(), **{})(fun4)

# Test that we can pass None to a function with an int argument
def fun5(arg):
    pass
fun5(None)

# Test that we can pass None to a function with a float argument
def fun6(arg):
    pass
fun6(None)

# Test that we can pass None to a function with a str argument
def fun7(arg):
    pass
fun7(None)

# Test that we can pass None to a function with a bytes
