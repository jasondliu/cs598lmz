from types import FunctionType
list(FunctionType(f.__code__, globals(), *f.__defaults__))

type(f)
type(f.__code__)
type(f.__defaults__)

help(f)
f.__doc__
f.__name__
f.__dict__
f.__code__.co_varnames
f.__code__.co_argcount

def f(x,y=1,z=2): ...
f.__defaults__ == (1, 2)
f.__kwdefaults__ == {'y': 1, 'z': 2}

# Functional programming

def add(x, y):
    return x+y

def mul(x, y):
    return x*y

def apply(f, x, y):
    return f(x,y)

apply(add, 2, 3)
apply(mul, 2, 3)

apply(lambda x,y: x+y, 2, 3)
apply(lambda x,y: x*y, 2, 3)

# Closures

# Cl
