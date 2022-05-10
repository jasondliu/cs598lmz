from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that we can create a function with a closure
def f(x):
    def g(y):
        return x + y
    return g

g = f(1)
assert g(2) == 3

# Test that we can create a function with a closure that uses a cell
def f(x):
    def g(y):
        return x + y
    x = 2
    return g

g = f(1)
assert g(2) == 3

# Test that we can create a function with a closure that uses a freevar
def f(x):
    def g(y):
        return x + y
    return g

x = 1
g = f(x)
assert g(2) == 3

# Test that we can create a function with a closure that uses a freevar
# that is a cell
def f(x):
    def g(y):
        return x + y
    return g

x = 1
g = f(x)
x = 2
assert g(2) ==
