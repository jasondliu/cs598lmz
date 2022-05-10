import types
# Test types.FunctionType
def test_types_function_type():
    def a():
        pass
    assert isinstance(a, types.FunctionType)
    assert types.FunctionType is type(a)

@raises(TypeError)
def test_types_function_type_err():
    type(None)
    
# Test types.LambdaType
def test_types_lambda_type():
    f = lambda x: x
    assert isinstance(f, types.LambdaType)
    assert types.LambdaType is type(f)

@raises(TypeError)
def test_types_lambda_type_err():
    type(None)

# Test types.GeneratorType
def test_types_generator_type():
    def f():
        yield 1
    assert isinstance(f(), types.GeneratorType)
    assert types.GeneratorType is type(f())

@raises(TypeError)
def test_types_generator_type_err():
    type(None)

# Test types.BuiltinFunctionType
@raises(Type
