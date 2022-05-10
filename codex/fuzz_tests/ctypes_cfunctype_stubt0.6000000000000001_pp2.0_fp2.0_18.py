import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 'hello'

print fun()

print type(fun)

class A(object):
    def __init__(self):
        self.a = 1

    def __call__(self):
        return 'hello'

a = A()
print a()
print type(a)

def fun():
    return 'hello'

print fun.__name__
print fun.__doc__
print fun.__dict__
print fun.__module__
print fun.__class__
print fun.__code__
print fun.__globals__

def fun():
    return 'hello'

print fun()
print type(fun)

print fun.__class__
print fun.__code__
print fun.__code__.co_argcount
print fun.__code__.co_code
print fun.__code__.co_consts
print fun.__code__.co_consts[0]
print fun.__code__.co_consts[1]
print fun.__code__.co_consts[2]
print fun.
