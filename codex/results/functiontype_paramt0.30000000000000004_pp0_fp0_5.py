from types import FunctionType
list(FunctionType(x, globals(), 'x') for x in (lambda: 1, lambda: 2))

# Test that the __name__ is set correctly
def f():
    pass
f.__name__

# Test that the __qualname__ is set correctly
def g():
    def h():
        pass
    h.__qualname__

# Test that the __annotations__ is set correctly
def f(x: 'x', y: 'y'):
    pass
f.__annotations__

# Test that the __kwdefaults__ is set correctly
def f(x, y=1, *, z=2):
    pass
f.__kwdefaults__

# Test that the __defaults__ is set correctly
def f(x, y=1, *args):
    pass
f.__defaults__

# Test that the __code__ is set correctly
def f():
    pass
f.__code__

# Test that the __globals__ is set correctly
def f():
    pass
f.__globals__

# Test that the __dict
