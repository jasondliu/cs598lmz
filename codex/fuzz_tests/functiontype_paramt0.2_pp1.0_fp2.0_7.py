from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda') for _ in range(10))

# Test that we can create a function with a closure that has a cell with a
# function.
def f(x):
    def g(y):
        return x + y
    return g

def h(x):
    return f(x)

list(h(x) for x in range(10))

# Test that we can create a function with a closure that has a cell with a
# function that has a closure.
def f(x):
    def g(y):
        def h(z):
            return x + y + z
        return h
    return g

def i(x):
    return f(x)

list(i(x)(x) for x in range(10))

# Test that we can create a function with a closure that has a cell with a
# function that has a closure that has a cell with a function.
def f(x):
    def g(y):
        def h(z):
            def i(w):
                return x + y + z
