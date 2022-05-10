import types
# Test types.FunctionType
def test_types_FunctionType():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert not isinstance(1, types.FunctionType)
    assert not isinstance(None, types.FunctionType)

# Test types.LambdaType
def test_types_LambdaType():
    l = lambda: None
    assert isinstance(l, types.LambdaType)
    assert not isinstance(1, types.LambdaType)
    assert not isinstance(None, types.LambdaType)

# Test types.GeneratorType
def test_types_GeneratorType():
    def f():
        yield 1
    g = f()
    assert isinstance(g, types.GeneratorType)
    assert not isinstance(1, types.GeneratorType)
    assert not isinstance(None, types.GeneratorType)

# Test types.CodeType
def test_types_CodeType():
    def f():
        pass
    assert isinstance(f.__code__, types.CodeType)
   
