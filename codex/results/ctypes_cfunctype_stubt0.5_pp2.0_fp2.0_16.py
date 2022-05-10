import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

@functools.wraps(fun)
def fun():
    return 1

def fun():
    return 1
fun.__name__ = 'fun'
fun.__module__ = 'test'

def fun():
    return 1
fun.__name__ = 'fun'
fun.__module__ = 'test'
fun.__wrapped__ = fun

def fun():
    return 1
fun.__name__ = 'fun'
fun.__module__ = 'test'
fun.__wrapped__ = fun
fun.__annotations__ = {'return': int}

def fun():
    return 1
fun.__name__ = 'fun'
fun.__module__ = 'test'
fun.__wrapped__ = fun
fun.__annotations__ = {'return': int}
fun.__qualname__ = 'fun'

def fun():
    return 1
fun.__name__ = 'fun'
fun.__module__ = 'test'
fun.__wrapped__ = fun
fun.__annotations__ = {'return':
