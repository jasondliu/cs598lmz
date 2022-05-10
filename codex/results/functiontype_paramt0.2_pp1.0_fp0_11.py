from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda') for _ in range(10))

# Test that the function name is not leaked.
def f():
    pass

f.__name__ = 'leaked'
list(FunctionType(lambda: None, globals(), 'lambda') for _ in range(10))

# Test that the function closure is not leaked.
def f():
    x = 1
    return lambda: x

f().__closure__
list(FunctionType(lambda: None, globals(), 'lambda') for _ in range(10))

# Test that the function dict is not leaked.
def f():
    pass

f.__dict__['leaked'] = 1
list(FunctionType(lambda: None, globals(), 'lambda') for _ in range(10))

# Test that the function annotations are not leaked.
def f():
    pass

f.__annotations__['leaked'] = 1
list(FunctionType(lambda: None, globals(), 'lambda') for _ in range(10))

# Test that the function defaults are not leaked.
def f(
