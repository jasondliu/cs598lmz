import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return object()

def f():
    fun()
f()

@FUNTYPE
def fun():
    return 5

def f():
    fun()
f()

class A(object):
    pass

def f():
    A.foo = 1

try:
    f()
except:
    pass

def f():
    A.foo = 2

f()
print A.foo

def f():
    A.foo = 1
A.foo = 2
print A.foo
f()
print A.foo

A.foo = 1
def f():
    A.foo = 2
print A.foo
f()
print A.foo

def f():
    A.foo = 1
A.foo = 2
print A.foo
f()
print A.foo

A.foo = 1
def f():
    A.foo = 2
print A.foo
f()
print A.foo

A.foo = 1
def f():
    A.foo = 2
print A.foo
f()
print A.foo


