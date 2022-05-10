from types import FunctionType
list(FunctionType(lambda x:x, {}).__code__.co_varnames)

import inspect
inspect.getargspec(lambda x:x)

def f(x, y=1):
    print(x, y)

inspect.getargspec(f)

def f(x, y=1, *args):
    print(x, y, args)

inspect.getargspec(f)

def f(x, y=1, *args, **kwargs):
    print(x, y, args, kwargs)

inspect.getargspec(f)

def f(x, y=1, *args, **kwargs):
    print(x, y, args, kwargs)

inspect.getargspec(f)

def f(x, y=1, *args, **kwargs):
    print(x, y, args, kwargs)

inspect.getargspec(f)

def f(x, y=1, *args, **kwargs):
    print(x, y, args
