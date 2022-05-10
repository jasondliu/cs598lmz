import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def call_int_int(fn, x):
    fn = FUNTYPE(fn)
    return fn(x)

@jit(nopython=True)
def f(x):
    return x + 1

assert call_int_int(f, 41) == 42

@jit(nopython=True)
def f(x):
    return x + 1

assert call_int_int(f.ctypes, 41) == 42

@jit(nopython=True)
def f(x):
    return x + 1

class Foo(object):
    pass

foo = Foo()
foo.bar = f
assert call_int_int(foo.bar.ctypes, 41) == 42
 

@jit(nopython=True)
def f(x):
    return x + 1

assert call_int_int(f.ctypes, 41) == 42

@jit(nopython=True)
def f(x):
    return x + 1

assert
