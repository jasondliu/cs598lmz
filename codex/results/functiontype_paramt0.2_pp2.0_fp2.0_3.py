from types import FunctionType
list(FunctionType(lambda x: x, globals()))

# code object
import dis
dis.dis(lambda x: x)

# function object
def f(x):
    return x

f.__code__
f.__code__.co_code
f.__code__.co_consts
f.__code__.co_names
f.__code__.co_varnames

# function object
def f(x):
    return x

f.__code__
f.__code__.co_code
f.__code__.co_consts
f.__code__.co_names
f.__code__.co_varnames

# function object
def f(x):
    return x

f.__code__
f.__code__.co_code
f.__code__.co_consts
f.__code__.co_names
f.__code__.co_varnames

# function object
def f(x):
    return x

f.__code__
f.__code__.co_code

