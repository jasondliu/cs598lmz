from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)

# ['<lambda>']

# Python 3.6+
def f():
    pass

list(f.__code__.co_varnames)

# ['f']

# Python 3.6+
def f(a, b, c, d):
    pass

list(f.__code__.co_varnames)

# ['a', 'b', 'c', 'd']

# Python 3.6+
def f(a, b, c, d, e=1, f=2, g=3):
    pass

list(f.__code__.co_varnames)

# ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Python 3.6+
def f(a, b, c, d, *args):
    pass

list(f.__code__.co_varnames)

# ['a', 'b', 'c', 'd', 'args']

# Python 3
