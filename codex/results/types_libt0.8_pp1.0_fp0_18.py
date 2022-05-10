import types
types.CodeType(0, 0, 0, 2, 67, b'', (), (), (), '', '', 0, b'')

# from a compiled code object

def f(x):
    return x + 1

co = f.__code__
co.co_argcount

def f():
    return lambda x: x

co = f().__code__
co.co_argcount

# non-public method of a code object

def f(a, b):
    pass

co = f.__code__
co.co_argcount
co.co_nlocals
types.CodeType._cached_internals_writeable = True
try:
    co._cached_internals = (a, b, c)
except TypeError:
    pass
else:
    print("FAIL")
types.CodeType._cached_internals_writeable = False

# code is immutable - attempts to change it should fail

def f(a):
    pass

co = f.__code__
co.co_argcount
types.CodeType.
