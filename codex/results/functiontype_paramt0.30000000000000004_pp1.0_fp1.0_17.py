from types import FunctionType
list(FunctionType(lambda: 0, globals(), 'foo') for i in range(10))

# Test that the code object is not shared between the functions.
def f():
    return f.__code__

def g():
    return g.__code__

f() is f()
g() is g()
f() is not g()

# Test that the default argument values are not shared between the functions.
def f(a=[]):
    return a

def g(a=[]):
    return a

f() is f()
g() is g()
f() is not g()

# Test that the closure cells are not shared between the functions.
def f(x):
    def g(y):
        return x + y
    return g

def h(x):
    def g(y):
        return x + y
    return g

f(1)(2)
h(1)(2)
f(1).__closure__[0].cell_contents
h(1).__closure__[0].cell_contents
f(1).__closure__[0
