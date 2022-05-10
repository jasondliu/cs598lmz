import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 3

assert(fun() == 3)

@ctypes.CFUNCTYPE(ctypes.py_object)
def fun():
    return 3

assert(fun() == 3)
 
assert(ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_char*4) is ctypes.CFUNCTYPE(None, ctypes.c_int, ctypes.c_int))

@ctypes.CFUNCTYPE(ctypes.py_object, ctypes.py_object)
def py_fun(x):
    return x

assert(3 == py_fun(3))
assert(3 == py_fun(ctypes.py_object(3)))

# test for https://bitbucket.org/pypy/pypy/issues/2888
import ctypes
def c_fun():
    return 1
c_fun = ctypes.CFUNCTYPE(ctypes.c_int64)(c_fun)
assert ctypes.c_int64() == c_fun()
