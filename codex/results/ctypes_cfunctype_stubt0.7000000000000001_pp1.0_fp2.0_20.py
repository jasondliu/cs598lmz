import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 42
fun()

def foo(x):
    return x
def boop():
    return foo
foo = boop
foo(42)

def foo(x):
    return x
foo = lambda x:x
foo(42)

def foo(x):
    return x
foo(42)
foo = lambda x:x

def foo(x):
    return x
foo = lambda x:x
foo(42)

def foo(x, y):
    return x + y
print foo(1, 2)

def foo(x, y):
    return x + y
print foo(1, 2)

def foo(x, y):
    pass

def foo(x, y):
    def bar(x):
        return x
    return x + y
print foo(1, 2)

def foo(x, y):
    def bar(x):
        return x
    return x + y
print foo(1, 2)

def foo(x, y):
    def bar(x):
        return x
    return x
