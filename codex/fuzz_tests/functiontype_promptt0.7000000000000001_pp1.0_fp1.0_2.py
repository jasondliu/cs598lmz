import types
# Test types.FunctionType

def f():
    pass
f.__name__

type(f)

def g():
    pass
g.__name__

type(g)

import inspect
inspect.getargspec(f)
inspect.getargspec(g)


def f(arg1, arg2, kwdarg1=None, kwdarg2=None):
    pass

inspect.getargspec(f)

def g(arg1, arg2, *args, **kw):
    pass

inspect.getargspec(g)


def f(arg1, arg2, kwdarg1=None, kwdarg2=None, *args, **kw):
    pass

inspect.getargspec(f)

#

class A:
    def f(self):
        pass

    def g(self):
        return lambda: None

a = A()

a.f.__name__

type(a.f)

a.g().__name__

type(a.g())

def f(
