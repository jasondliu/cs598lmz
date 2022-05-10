import types
# Test types.FunctionType(function)
def test_functiontype_function():
    def func():
        pass
    f = types.FunctionType(func.__code__, globals())
    assert f() is None

# Test types.FunctionType(function, globals)
def test_functiontype_function_globals():
    def func(x):
        return x + 1
    f = types.FunctionType(func.__code__, globals())
    assert f(2) == 3

# Test types.FunctionType(function, globals, name)
def test_functiontype_function_globals_name():
    def func(x):
        return x + 1
    f = types.FunctionType(func.__code__, globals(), "func")
    assert f(2) == 3
    assert f.__name__ == "func"
    assert f.__qualname__ == "func"

# Test types.FunctionType(function, globals, name, closure)
def test_functiontype_function_globals_name_closure():
    def func(x):
       
