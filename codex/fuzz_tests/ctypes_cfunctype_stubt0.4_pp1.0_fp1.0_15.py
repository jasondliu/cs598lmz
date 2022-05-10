import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

fun()

# The following is a very common mistake:

@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 42

fun()

# This fails with the following error:

# TypeError: 'CFUNCTYPE' object is not callable

# The reason is that the decorator is called immediately, and does not
# return a function object.  Instead, it returns a type object, which
# cannot be called.  The solution is to use a lambda expression:

@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return lambda: 42

fun()()
