import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'fun'

f = fun
print f()

def fun():
    return 'fun'

f = FUNTYPE(fun)
print f()

f = FUNTYPE(lambda: 'fun')
print f()
