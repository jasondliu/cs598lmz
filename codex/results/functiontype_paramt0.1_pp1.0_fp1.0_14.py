from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo'))

# Test that we can create a function with a closure
def f(x):
    def g(y):
        return x + y
    return g

f(1)(2)

# Test that we can create a function with a closure that references a global
def f(x):
    def g(y):
        return x + y + z
    return g

z = 1
f(1)(2)

# Test that we can create a function with a closure that references a global
# that is a function
def f(x):
    def g(y):
        return x + y + z()
    return g

def z():
    return 1

f(1)(2)

# Test that we can create a function with a closure that references a global
# that is a function that references a global
def f(x):
    def g(y):
        return x + y + z()
    return g

def z():
    return 1 + w

w = 1
f(1)(2)

# Test
