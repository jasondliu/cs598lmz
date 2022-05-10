import types
# Test types.FunctionType
def test_function_type():
    assert isinstance(test_function_type, types.FunctionType)
    assert isinstance(types.FunctionType, types.FunctionType)
    assert not isinstance(1, types.FunctionType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(test_builtin_function_type, types.BuiltinFunctionType)
    assert isinstance(len, types.BuiltinFunctionType)
    assert not isinstance(1, types.BuiltinFunctionType)

# Test types.LambdaType
def test_lambda_type():
    assert isinstance((lambda x: x), types.LambdaType)
    assert not isinstance((lambda x: x)(1), types.LambdaType)

# Test types.GeneratorType
def test_generator_type():
    assert isinstance((x for x in range(3)), types.GeneratorType)
    assert not isinstance(1, types.GeneratorType)

# Test types.CodeType
def test_code_type():
