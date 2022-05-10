from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))

# code objects
import dis
def f(x):
    return x
dis.dis(f)

# bytecode
def f(x):
    return x
f.__code__.co_code

# bytecode
def f(x):
    return x
f.__code__.co_code

# bytecode
def f(x):
    return x
f.__code__.co_code

# bytecode
def f(x):
    return x
f.__code__.co_code

# bytecode
def f(x):
    return x
f.__code__.co_code

# bytecode
def f(x):
    return x
f.__code__.co_code

# bytecode
def f(x):
    return x
f.__code__.co_code

# bytecode
def f(x):
    return x
f.__code__.co_code

# bytecode
def f(x):
    return x
f.
