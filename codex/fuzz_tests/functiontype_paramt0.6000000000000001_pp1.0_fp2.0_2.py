from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, "foo", (), None).__closure__)

# tuple
t = (lambda: 1).__closure__
type(t)
t[0].cell_contents
t[0].cell_contents = 42

def f():
    x = 2
    y = 3
    return lambda: x + y

g = f()
g()

# function attributes
def f():
    "foo"

f.__name__
f.__doc__
f.__module__
f.__code__
f.__code__.co_varnames
f.__code__.co_argcount
f.__defaults__
f.__closure__
f.__dict__

# function attributes
def f():
    "foo"

f.__name__
f.__doc__
f.__module__
f.__code__
f.__code__.co_varnames
f.__code__.co_argcount
f.__defaults__
f.__closure__
f.
