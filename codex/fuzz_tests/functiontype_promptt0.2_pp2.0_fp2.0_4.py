import types
# Test types.FunctionType
def foo():
    pass

def bar():
    pass

def baz():
    pass

def test_function_type():
    assert isinstance(foo, types.FunctionType)
    assert isinstance(bar, types.FunctionType)
    assert isinstance(baz, types.FunctionType)

# Test types.LambdaType
def test_lambda_type():
    assert isinstance(lambda: None, types.LambdaType)
    assert isinstance(lambda x: x, types.LambdaType)
    assert isinstance(lambda x, y: x + y, types.LambdaType)

# Test types.GeneratorType
def test_generator_type():
    assert isinstance((x for x in range(10)), types.GeneratorType)
    assert isinstance((x for x in range(10) if x % 2 == 0), types.GeneratorType)

# Test types.CodeType
def test_code_type():
    assert isinstance(foo.__code__, types.CodeType)
    assert isinstance(bar.__
