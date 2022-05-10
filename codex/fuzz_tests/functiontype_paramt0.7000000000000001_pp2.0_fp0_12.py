from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, None, None, f.__closure__))

# a bit more complex
def f(a):
    b = 2
    c = 3
    def g(d):
        e = 4
        return a + b + c + d + e
    return g

list(FunctionType(f.__code__, f.__globals__, None, None, f.__closure__))

# but we can't do this directly:
FunctionType(f.__code__, f.__globals__, None, None, f.__closure__)

# we need the cell objects:
list(FunctionType(f.__code__, f.__globals__, None, None, f.__closure__).__closure__)

# and then we can do this:
FunctionType(f.__code__, f.__globals__, None, None, f.__closure__).__closure__

# let's create a new instance of `f`:
g = FunctionType(f.__code__,
