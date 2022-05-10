import types
# Test types.FunctionType
def func(): pass
assert isinstance(func, types.FunctionType)
assert func.__name__ == 'func'
assert func.__doc__ is None

def func2(a, b, c): pass
assert func2.__name__ == 'func2'
assert func2.__doc__ is None

def func3(a, b, c, *args): pass
assert func3.__name__ == 'func3'
assert func3.__doc__ is None

def func4(a, b, c, **kwargs): pass
assert func4.__name__ == 'func4'
assert func4.__doc__ is None

def func5(a, b, c, *args, **kwargs): pass
assert func5.__name__ == 'func5'
assert func5.__doc__ is None

def func6(a, b, c, *, d, e, f): pass
assert func6.__name__ == 'func6'
assert func6.__doc__ is None

def func7(a, b, c, *args, d
