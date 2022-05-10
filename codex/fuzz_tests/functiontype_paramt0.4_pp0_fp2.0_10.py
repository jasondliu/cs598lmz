from types import FunctionType
list(FunctionType(f.__code__, globals(), 'f'))

# __code__.co_varnames
# __code__.co_argcount
# __code__.co_cellvars
# __code__.co_freevars

# __closure__

def f(x, y):
    x = 1
    y = 2
    def g(z):
        return x + y + z
    return g

f(1, 2)(3)

def f(x, y):
    x = 1
    y = 2
    def g(z):
        return x + y + z
    return g

f(1, 2).__closure__

def f(x, y):
    x = 1
    y = 2
    def g(z):
        return x + y + z
    return g

f(1, 2).__closure__[1].cell_contents

def f(x, y):
    x = 1
    y = 2
    def g(z):
        return x + y + z
    return g

