import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

@FUNTYPE
def fun2(x):
    return x

def foo():
    pass

print fun()

#print fun(1)

#print fun("hello")

print fun2("hi")

print ctypes.cast(foo, FUNTYPE)

print ctypes.cast(foo, ctypes.CFUNCTYPE(ctypes.c_int))
