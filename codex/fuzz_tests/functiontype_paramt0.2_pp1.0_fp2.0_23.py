from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# This is a function that takes a function and returns a function.
def compose(f, g):
    return lambda x: f(g(x))

# This is a function that takes a function and returns a function.
def compose2(f, g):
    return lambda *args, **kwargs: f(g(*args, **kwargs))

# This is a function that takes a function and returns a function.
def compose3(f, g):
    return lambda *args, **kwargs: f(g(*args, **kwargs))

# This is a function that takes a function and returns a function.
def compose4(f, g):
    return lambda *args, **kwargs: f(g(*args, **kwargs))

# This is a function that takes a function and returns a function.
def compose5(f, g):
    return lambda *args, **kwargs: f(g(*args, **kwargs))

# This is a function that takes a function and returns a function.
def compose6(f,
