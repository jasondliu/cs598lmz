import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert type(f) is types.FunctionType

# Test types.LambdaType
def test_lambda_type():
    f = lambda: None
    assert isinstance(f, types.LambdaType)
    assert type(f) is types.LambdaType

# Test types.GeneratorType
def test_generator_type():
    def f():
        yield None
    assert isinstance(f(), types.GeneratorType)
    assert type(f()) is types.GeneratorType

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(abs, types.BuiltinFunctionType)
    assert type(abs) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
def test_builtin_method_type():
    assert isinstance(''.__len__, types.BuiltinMethodType)
    assert type(''.__len__) is types.BuiltinMethodType
