from types import FunctionType
list(FunctionType(f.__code__, globals(), "foo"))

# code object
def f(x):
    return x + 1

f.__code__

# code object
def f(x):
    return x + 1

f.__code__.co_code

# code object
def f(x):
    return x + 1

f.__code__.co_code[0]

# code object
def f(x):
    return x + 1

f.__code__.co_code[0]

# code object
def f(x):
    return x + 1

f.__code__.co_code[0]

# code object
def f(x):
    return x + 1

f.__code__.co_code[0]

# code object
def f(x):
    return x + 1

f.__code__.co_code[0]

# code object
def f(x):
    return x + 1

f.__code__.co_code[0]

# code object
