from types import FunctionType
list(FunctionType(lambda: None, {}, 'foo', (), None))

# Test that the __name__ attribute is set correctly
def foo():
    pass
foo.__name__

# Test that the __qualname__ attribute is set correctly
def foo():
    pass
foo.__qualname__

# Test that the __module__ attribute is set correctly
def foo():
    pass
foo.__module__

# Test that the __defaults__ attribute is set correctly
def foo(a, b=1, c=2):
    pass
foo.__defaults__

# Test that the __code__ attribute is set correctly
def foo():
    pass
foo.__code__

# Test that the __closure__ attribute is set correctly
def foo():
    x = 1
    def bar():
        return x
    return bar
foo().__closure__

# Test that the __annotations__ attribute is set correctly
def foo(a: 1, b: 2 = 3, *args: 4, c: 5, d: 6 = 7, **kwargs: 8) -> 9:
    pass
foo.
