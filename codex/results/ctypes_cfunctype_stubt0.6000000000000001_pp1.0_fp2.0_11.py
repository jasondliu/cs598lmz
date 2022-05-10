import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"

fun()

FUNTYPE = ctypes.CFUNCTYPE(None, ctypes.py_object)
@FUNTYPE
def fun(x):
    print(x)

fun("hello")

c_fun = FUNTYPE(fun)
c_fun("hello")

from ctypes import c_void_p, c_int, c_char_p

def callback(a, b, c):
    print("callback called", a, b, c)

c_callback = FUNTYPE(callback)

lib.callback(c_callback, c_void_p(1), c_int(2), c_char_p("3".encode("ascii")))
</code>

