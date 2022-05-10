from types import FunctionType
list(FunctionType(lambda x: x**2, globals(), 'f')(i) for i in range(5))

# this is equivalent to
def f(x):
    return x**2
list(f(i) for i in range(5))

def g(x, y):
    return (y**2 - x**2) / (2*x*y)

def h(*args):
    x = args[0]
    for i in range(len(args) - 1):
        x = g(x, args[i+1])
    return x

h(0.1, 0.11, 0.12, 0.13)

# The same as
def h(x, *args):
    for arg in args:
        x = g(x, arg)
    return x

h(0.1, 0.11, 0.12, 0.13)

# The same as
def h(*args):
    x = args[0]
    for y in args[1:]:
        x = g(x, y)
    return x

h
