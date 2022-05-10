import types
# Test types.FunctionType
def test_function_type():
    def foo():
        pass
    assert type(foo) == types.FunctionType
    assert type(lambda: None) == types.FunctionType
    assert type(test_function_type) == types.FunctionType

# Test types.LambdaType
def test_lambda_type():
    assert type(lambda: None) == types.LambdaType

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert type(len) == types.BuiltinFunctionType
    assert type(test_builtin_function_type) == types.BuiltinFunctionType

# Test types.GeneratorType
def test_generator_type():
    def foo():
        yield 1
    assert type(foo()) == types.GeneratorType
    assert type((i for i in range(10))) == types.GeneratorType

# Test types.GeneratorType
def test_code_type():
    def foo(): pass
    assert type(foo.__code__) == types.CodeType
    assert type(test_code_
