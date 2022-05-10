import types
# Test types.FunctionType
def foo(x):
    return x+1

def test_function_type():
    assert isinstance(foo, types.FunctionType)
    assert isinstance(test_function_type, types.FunctionType)

# Test types.BuiltinFunctionType
def test_builtinfunction_type():
    assert isinstance(len, types.BuiltinFunctionType)
    assert isinstance(foo, types.BuiltinFunctionType)

# Test types.MethodType
def test_method_type():
    assert isinstance("foo".upper, types.MethodType)
    assert isinstance("foo".__add__, types.MethodType)

# Test types.LambdaType
def test_lambda_type():
    assert isinstance(lambda x: x+1, types.LambdaType)

# Test types.GeneratorType
def generator():
    yield 1

def test_generator_type():
    assert isinstance(generator(), types.GeneratorType)

# Test types.CodeType
def test_code_type():
    assert isinstance(foo.__code
