import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

fun()

@FUNTYPE
def fun():
    print 'ret'
    return 'hello'

fun()

@FUNTYPE
def fun(a,b):
    print 'ret'
    return a+b

fun('a','b')

@FUNTYPE
def fun(a,b):
    print 'ret'
    return a+b

fun()
