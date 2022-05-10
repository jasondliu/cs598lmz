from types import FunctionType
list(FunctionType(lambda: None, globals(), 'lambda'))

# Test that the __name__ attribute is set correctly
def f(): pass
f.__name__

# Test that the __qualname__ attribute is set correctly
def f(): pass
f.__qualname__

# Test that the __module__ attribute is set correctly
def f(): pass
f.__module__

# Test that the __defaults__ attribute is set correctly
def f(a, b=1): pass
f.__defaults__

# Test that the __kwdefaults__ attribute is set correctly
def f(a, b=1, *, c=2): pass
f.__kwdefaults__

# Test that the __annotations__ attribute is set correctly
def f(a: 1, b: 2 = 1, *, c: 3 = 2): pass
f.__annotations__

# Test that the __closure__ attribute is set correctly
def f():
    x = 1
    def g():
        return x
    return g
f().__closure__

# Test that the __code__ attribute is set correctly
