import types
# Test types.FunctionType
def test_function_type():
    def f(): pass
    assert isinstance(f, types.FunctionType)
    assert not isinstance(1, types.FunctionType)
    assert not isinstance(1.5, types.FunctionType)
    assert not isinstance('', types.FunctionType)
    assert not isinstance(u'', types.FunctionType)
    assert not isinstance(True, types.FunctionType)
    assert not isinstance(None, types.FunctionType)
    assert not isinstance(object(), types.FunctionType)

# Test types.LambdaType
def test_lambda_type():
    f = lambda: None
    assert isinstance(f, types.LambdaType)
    assert not isinstance(1, types.LambdaType)
    assert not isinstance(1.5, types.LambdaType)
    assert not isinstance('', types.LambdaType)
    assert not isinstance(u'', types.LambdaType)
    assert not isinstance(True, types.LambdaType)
    assert not isinstance
