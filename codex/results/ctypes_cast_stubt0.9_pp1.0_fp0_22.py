import ctypes
ctypes.cast(id(x), ctypes.py_object).value

# Initialize `f` with parameter `x`
f = x
print('id(x):', id(x))
print('id(f):', id(f))
print('id(x) == id(f):', id(x) == id(f))

# Not touching `x`
print(x)

# Here we go
f[:] = 0
# What happened?
print(x)

# Note: call by sharing=reference
import inspect
print(inspect.signature(f))

# Demo: dictionary
cache = {}
error = ArithmeticError('something wrong')

def f(x):
    """Return x**2"""
    print('Computing f(x) ...')
    return x ** 2

def g(x):
    if x not in cache:
        if x == 2:
            # raise error
            raise error
        # put item in cache 
        cache[x] = f(x)
    return cache[x]

# Demo
g(3)


