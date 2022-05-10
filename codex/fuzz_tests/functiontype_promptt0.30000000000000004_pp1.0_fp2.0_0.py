import types
# Test types.FunctionType
def foo():
    pass

def bar():
    pass

def baz():
    pass

def test_types_FunctionType():
    assert isinstance(foo, types.FunctionType)
    assert isinstance(bar, types.FunctionType)
    assert isinstance(baz, types.FunctionType)

# Test types.BuiltinFunctionType
def test_types_BuiltinFunctionType():
    assert isinstance(len, types.BuiltinFunctionType)
    assert isinstance(abs, types.BuiltinFunctionType)
    assert isinstance(range, types.BuiltinFunctionType)

# Test types.GeneratorType
def test_types_GeneratorType():
    def foo():
        yield 1
        yield 2
    assert isinstance(foo(), types.GeneratorType)

# Test types.CodeType
def test_types_CodeType():
    assert isinstance(foo.__code__, types.CodeType)
    assert isinstance(bar.__code__, types.CodeType)
    assert isinstance(baz.__code__, types.CodeType)
