import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print 'hello'
    return 'a', 2, [1, 2]

globals()['fun'] = fun

fun.__name__ = 'fun'
fun.__module__ = __name__

def f():
    print fun()

f()
