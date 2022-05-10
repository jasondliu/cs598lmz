from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# Code objects
import dis
dis.dis(lambda: None)
dis.dis(lambda x: x)
dis.dis(lambda x, y: x + y)

# Function attributes
def f(): pass
f.__name__
f.__doc__
f.__module__
f.__defaults__
f.__code__
f.__globals__
f.__dict__

# Function annotations
def f(a: 'annotation'): pass
f.__annotations__

# Function introspection
def f(a, b, *args, c, d=42, **kwargs): pass
f.__code__.co_varnames
f.__code__.co_argcount
f.__defaults__
f.__kwdefaults__

# Function objects
def f(): pass
f.__closure__
f.__closure__[0].cell_contents

# Function objects
def f(x):
    def g(y):
        return x + y
    return g
