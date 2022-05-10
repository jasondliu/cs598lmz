import types
# Test types.FunctionType
def test_function_type():
    def func(): pass
    assert isinstance(func, types.FunctionType)

# from types import FunctionType
# Test types.FunctionType
def test_function_type():
    def func(): pass
    assert isinstance(func, FunctionType)

# Test user-defined function type
class MyFunction(object):
    def __call__(self):
        pass

def test_user_defined_function_type():
    assert isinstance(lambda: None, MyFunction)

# Test unwrapped built-in type
def test_unwrapped_builtin_type():
    assert isinstance(1, int)

# Test unwrapped built-in type of type
def test_unwrapped_builtin_type_of_type():
    assert isinstance(int, type)

# Test wrapped built-in type
def test_wrapped_builtin_type():
    def _(x):
        return isinstance(x, int)
    assert _(1)

# Test wrapped built-in type of type
def test_
