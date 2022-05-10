import types
# Test types.FunctionType
def function_call(func, *args, **kwargs):
    return func(*args, **kwargs)

def test_function_call():
    def f(x, y):
        return x + y
    assert function_call(f, 1, y=2) == 3
    assert function_call(f, 1, 2) == 3

def test_function_call_with_defaults():
    def f(x, y=1):
        return x + y
    assert function_call(f, 1) == 2
    assert function_call(f, 1, y=2) == 3

def test_function_call_with_starargs():
    def f(x, *args):
        return x + sum(args)
    assert function_call(f, 1, 2, 3) == 6
    assert function_call(f, 1, *(2, 3)) == 6

def test_function_call_with_kwargs():
    def f(x, **kwargs):
        return x + sum(kwargs.values())
    assert function_call
