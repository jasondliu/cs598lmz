from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# Test that the repr of a function is evaluable.
def f(): pass
repr(f)

# Test that the repr of a function with a closure is evaluable.
def f():
    x = 1
    def g():
        return x
    return g
repr(f())

# Test that the repr of a function with a closure with free vars is evaluable.
def f():
    x = 1
    def g():
        return x
    return g
repr(f()())

# Test that the repr of a function with a closure with free vars is evaluable.
def f():
    x = 1
    def g():
        return x
    return g
repr(f()())

# Test that the repr of a function with a closure with free vars is evaluable.
def f():
    x = 1
    def g():
        return x
    return g
repr(f()())

# Test that the repr of a function with a closure with free vars is evaluable.
def f
