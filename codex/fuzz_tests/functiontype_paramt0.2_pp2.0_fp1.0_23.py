from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda').__code__.co_varnames)

def f(x, y):
    return x + y

list(f.__code__.co_varnames)

def f(x, y, z=1):
    return x + y + z

list(f.__code__.co_varnames)

def f(x, y, z=1, *args):
    return x + y + z

list(f.__code__.co_varnames)

def f(x, y, z=1, *args, **kwargs):
    return x + y + z

list(f.__code__.co_varnames)

def f(x, y, z=1, *args, **kwargs):
    return x + y + z

list(f.__code__.co_varnames)

def f(x, y, z=1, *args, **kwargs):
    return x + y + z

list(f.__code__.co
