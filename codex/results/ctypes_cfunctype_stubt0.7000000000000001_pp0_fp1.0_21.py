import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
assert fun() == 42

@FUNTYPE
def fun():
    return "hello"
assert fun() == "hello"

@functools.singledispatch
def fun(arg):
    return arg

@fun.register(int)
def _(arg):
    return arg + 5

assert fun(5) == 10
assert fun('hello') == 'hello'
