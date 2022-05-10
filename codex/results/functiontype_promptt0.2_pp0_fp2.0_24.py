import types
# Test types.FunctionType
def f(): pass
def g(): pass
def h(): pass

def test_function_type():
    assert isinstance(f, types.FunctionType)
    assert isinstance(g, types.FunctionType)
    assert isinstance(h, types.FunctionType)
    assert not isinstance(42, types.FunctionType)
    assert not isinstance(None, types.FunctionType)
    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(g, types.BuiltinFunctionType)
    assert not isinstance(h, types.BuiltinFunctionType)
    assert not isinstance(42, types.BuiltinFunctionType)
    assert not isinstance(None, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    import sys
    assert isinstance(sys.exit, types.BuiltinFunctionType)
    assert isinstance(sys.getrefcount, types.BuiltinFunctionType)
    assert isinstance(sys.getrefcount, types.FunctionType)
    assert not isinstance
