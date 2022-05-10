import types
# Test types.FunctionType
def f(): pass
def g(): pass
def h(): pass

def test_FunctionType():
    assert isinstance(f, types.FunctionType)
    assert isinstance(g, types.FunctionType)
    assert isinstance(h, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(g, types.BuiltinFunctionType)
    assert not isinstance(h, types.BuiltinFunctionType)
    assert not isinstance(f, types.MethodType)
    assert not isinstance(g, types.MethodType)
    assert not isinstance(h, types.MethodType)
    assert not isinstance(f, types.BuiltinMethodType)
    assert not isinstance(g, types.BuiltinMethodType)
    assert not isinstance(h, types.BuiltinMethodType)
    assert not isinstance(f, types.LambdaType)
    assert not isinstance(g, types.LambdaType)
    assert not isinstance(h, types.LambdaType)
    assert not isinstance(
