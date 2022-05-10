import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

def f():
    fun(None)

f()

# at least, this doesn't crash.

# Issue #2849: the repr() of a ctypes callback function should not
# cause a crash.

def f(x):
    pass

@ctypes.CFUNCTYPE(None, ctypes.c_int)
def g(x):
    print(x)

print(repr(g))
print(repr(f))

# Issue #2935: callbacks calling callbacks

import ctypes

def f(x):
    print(x)

@ctypes.CFUNCTYPE(None, ctypes.c_int)
def g(x):
    f(x)

@ctypes.CFUNCTYPE(None, ctypes.c_int)
def h(x):
    g(x)

f(42)
g(42)
h(42)

# Issue #2838: ctypes callback with a ctypes.py_object argument

import ctypes

