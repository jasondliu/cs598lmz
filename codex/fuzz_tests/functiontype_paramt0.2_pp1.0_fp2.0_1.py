from types import FunctionType
list(FunctionType(lambda: None, globals(), 'foo') for _ in range(10))

# Test that the function name is not copied from the default argument
def f(x=f):
    return x.__name__
f()

# Test that the function name is not copied from the default argument
def f(x=f):
    return x.__name__
f()

# Test that the function name is not copied from the default argument
def f(x=f):
    return x.__name__
f()

# Test that the function name is not copied from the default argument
def f(x=f):
    return x.__name__
f()

# Test that the function name is not copied from the default argument
def f(x=f):
    return x.__name__
f()

# Test that the function name is not copied from the default argument
def f(x=f):
    return x.__name__
f()

# Test that the function name is not copied from the default argument
def f(x=f):
    return x.__name__
f()
