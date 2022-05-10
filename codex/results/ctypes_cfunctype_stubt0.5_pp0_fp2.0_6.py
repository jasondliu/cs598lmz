import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

@jit(nopython=True)
def foo():
    return fun()

foo()
 
@jit(nopython=True)
def foo():
    return fun()

foo()
 
@jit(nopython=True)
def foo():
    return fun()

foo()
 
@jit(nopython=True)
def foo():
    return fun()

foo()
 
@jit(nopython=True)
def foo():
    return fun()

foo()
 
@jit(nopython=True)
def foo():
    return fun()

foo()
 
@jit(nopython=True)
def foo():
    return fun()

foo()
 
@jit(nopython=True)
def foo():
    return fun()

foo()
 
@jit(nopython=True)
def foo():
    return fun()

foo()
 
@jit(nopython=True)
def foo():
    return fun()

foo()
 

