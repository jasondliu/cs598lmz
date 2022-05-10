import ctypes
ctypes.cast(0, ctypes.py_object)

# ____________________________________________________________

class X(object):
    pass

def f():
    return X()

def g():
    x = X()
    x.foo = 42
    return x

def h():
    x = X()
    x.foo = "hello"
    return x

def j():
    x = X()
    x.foo = 42
    x.bar = "hello"
    return x

def k():
    x = X()
    x.foo = 42
    x.bar = "hello"
    x.baz = "world"
    return x

def l():
    x = X()
    x.foo = 42
    x.bar = "hello"
    x.baz = "world"
    x.qux = "!"
    return x

def m():
    x = X()
    x.foo = 42
    x.bar = "hello"
    x.baz = "world"
    x.qux = "!"
    x.sp
