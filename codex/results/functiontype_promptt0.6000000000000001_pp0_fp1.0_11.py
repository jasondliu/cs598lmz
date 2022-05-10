import types
# Test types.FunctionType
def test_function_type():
    def f(): pass
    assert isinstance(f, types.FunctionType)
    assert issubclass(types.FunctionType, object)

def test_function_type_attributes():
    def f(): pass
    assert f.__name__ == 'f'
    assert f.__doc__ is None
    assert f.__module__ == __name__

def test_function_type_attributes_2():
    def f(): "docstring"
    assert f.__name__ == 'f'
    assert f.__doc__ == "docstring"
    assert f.__module__ == __name__

def test_function_type_attributes_3():
    def f(): "docstring"
    f.attr = 42
    assert f.attr == 42

def test_function_type_attributes_4():
    def f(): "docstring"
    f.foo = f.__doc__
    assert f.foo == "docstring"

def test_function_type_call():
    def f(x):

