import types
# Test types.FunctionType
def test_types_FunctionType():
    def f():
        pass
    assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
def test_types_BuiltinFunctionType():
    assert type(abs) is types.BuiltinFunctionType

# Test types.LambdaType
def test_types_LambdaType():
    assert type(lambda: 0) is types.LambdaType

# Test types.GeneratorType
def test_types_GeneratorType():
    def f():
        yield 0
    assert type(f()) is types.GeneratorType

# Test types.CodeType
def test_types_CodeType():
    def f():
        pass
    assert type(f.__code__) is types.CodeType

# Test types.MappingProxyType
def test_types_MappingProxyType():
    d = {'a': 1}
    assert type(types.MappingProxyType(d)) is types.MappingProxyType

# Test types.SimpleNamespace
def test_types_SimpleNamespace():

