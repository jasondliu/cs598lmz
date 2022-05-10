import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "Hello World"
fun()

type(fun)

class Foo(ctypes.Structure):
    _fields_ = [("n", ctypes.c_int)]

FOO_OBJ = ctypes.POINTER(Foo)
FOO_OBJ = ctypes.POINTER(Foo)

@FUNTYPE
def fun(obj):
    return obj.contents.n
a = Foo()
a.n = 42
fun(a)

class Bar(ctypes.Structure):
    _fields_ = [("n", ctypes.c_int)]

BAR_OBJ = ctypes.POINTER(Bar)

@FUNTYPE
def fun(obj):
    return obj.contents.n #!
a = Bar()
a.n = 42
fun(a)

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.py_object)
@FUNTYPE
def fun(obj):
    return obj.n
a = Bar()
a.n = 42
fun
