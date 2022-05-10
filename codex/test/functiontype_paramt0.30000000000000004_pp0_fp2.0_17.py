from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in (lambda: None, lambda x: None, lambda x, y: None))

# Test that we can create a function with a non-None closure
def f(x):
    y = 2
    def g(z):
        return x + y + z
    return g

g = f(1)
assert g.__closure__[0].cell_contents == 1
assert g.__closure__[1].cell_contents == 2
assert g(3) == 6

# Test that we can create a function with a non-None closure, and a non-None
# __defaults__
def f(x):
    y = 2
    def g(z, w=3):
        return x + y + z + w
    return g

g = f(1)
assert g.__closure__[0].cell_contents == 1
