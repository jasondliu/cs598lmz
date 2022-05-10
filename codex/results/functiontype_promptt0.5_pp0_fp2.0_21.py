import types
# Test types.FunctionType
def test_types_FunctionType():
    def foo():
        pass
    assert isinstance(foo, types.FunctionType)
    assert isinstance(test_types_FunctionType, types.FunctionType)
    assert not isinstance(None, types.FunctionType)
    assert not isinstance(foo, types.BuiltinFunctionType)

# Test types.LambdaType
def test_types_LambdaType():
    f = lambda x: x
    assert isinstance(f, types.LambdaType)
    assert not isinstance(test_types_LambdaType, types.LambdaType)

# Test types.GeneratorType
def test_types_GeneratorType():
    def foo():
        yield 1
    g = foo()
    assert isinstance(g, types.GeneratorType)
    assert not isinstance(foo, types.GeneratorType)
    assert not isinstance(test_types_GeneratorType, types.GeneratorType)

# Test types.CodeType
def test_types_CodeType():
    def foo():
        pass

