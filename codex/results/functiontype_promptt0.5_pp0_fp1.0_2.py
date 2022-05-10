import types
# Test types.FunctionType

def foo():
    pass

def bar():
    pass

def baz():
    pass

def test_function_type():
    assert isinstance(foo, types.FunctionType)
    assert isinstance(bar, types.FunctionType)
    assert isinstance(baz, types.FunctionType)
    assert not isinstance(1, types.FunctionType)
    assert not isinstance("str", types.FunctionType)
    assert not isinstance(None, types.FunctionType)
    assert not isinstance(object(), types.FunctionType)

def test_function_type_name():
    assert foo.__name__ == 'foo'
    assert bar.__name__ == 'bar'
    assert baz.__name__ == 'baz'

def test_function_type_repr():
    assert repr(foo) == '<function foo at 0x%x>' % foo.__code__.co_firstlineno
    assert repr(bar) == '<function bar at 0x%x>' % bar.__code__.co_firstlineno
   
