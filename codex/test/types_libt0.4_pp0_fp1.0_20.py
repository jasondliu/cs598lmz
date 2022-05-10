import types
types.MethodType(lambda self: None, None, None)

# This is a syntax error in Python 2.
def f(x: int = ...):
    pass

# This is a syntax error in Python 2.
def f(x: ...):
    pass

# This is a syntax error in Python 2.
def f(x: int):
    pass

# This is a syntax error in Python 2.
def f(x: int = 1):
    pass

# This is a syntax error in Python 2.
def f(x: int = 1, *, y: int):
    pass

# This is a syntax error in Python 2.
def f(x: int = 1, *, y: int = 2):
    pass

# This is a syntax error in Python 2.
def f(x: int = 1, *, y: int = 2, **kwargs: int):
    pass

# This is a syntax error in Python 2.
