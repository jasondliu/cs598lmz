import types
# Test types.FunctionType

def f():
    pass

def g():
    pass

def h():
    pass

def test_function_type():
    assert isinstance(f, types.FunctionType)
    assert isinstance(g, types.FunctionType)
    assert isinstance(h, types.FunctionType)
    assert not isinstance(1, types.FunctionType)
    assert not isinstance(1.0, types.FunctionType)
    assert not isinstance("1", types.FunctionType)
    assert not isinstance(None, types.FunctionType)
    assert not isinstance([1], types.FunctionType)
    assert not isinstance((1,), types.FunctionType)
    assert not isinstance({1:1}, types.FunctionType)
    assert not isinstance(set([1]), types.FunctionType)
    assert not isinstance(frozenset([1]), types.FunctionType)
    assert not isinstance(object(), types.FunctionType)
    assert not isinstance(object, types.FunctionType)
    assert not isinstance(types.FunctionType, types.FunctionType)
