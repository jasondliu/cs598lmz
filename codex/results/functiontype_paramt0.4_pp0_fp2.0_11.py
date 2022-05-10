from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__))

def f(*args, **kwargs):
    print(args, kwargs)
f.__code__.co_varnames
f.__code__.co_argcount

class MyClass:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

MyClass.__init__.__code__.co_varnames
MyClass.__init__.__code__.co_argcount

def f(*args, **kwargs):
    print(args, kwargs)

f.__code__.co_varnames
f.__code__.co_argcount

def f(a, b, c):
    print(a, b, c)

f.__code__.co_varnames
f.__code__.co_argcount

def f
