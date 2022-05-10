import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42

@jit("i8(i8)")
def f(x):
    return x

@jit("i8()")
def g():
    return f(42)

@jit("i8(i8(i8))")
def h(f):
    return f(42)

@jit("i8()")
def i():
    return h(f)

@jit("i8()")
def j():
    return h(g)

assert f(42) == 42
assert g() == 42
assert h(f) == 42
assert i() == 42
assert j() == 42

@jit("i8(i8)")
def f(x):
    return x + 1

@jit("i8()")
def g():
    return f(42)

@jit("i8(i8(i8))")
def h(f):
    return f(42)

@jit("i8()")
def i():
    return h(f)

@jit("i8()")
def j():
   
