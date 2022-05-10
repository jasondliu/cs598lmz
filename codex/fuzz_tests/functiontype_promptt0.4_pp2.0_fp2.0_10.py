import types
# Test types.FunctionType
def test_function_type():
    def f(): pass
    assert isinstance(f, types.FunctionType)
    assert isinstance(test_function_type, types.FunctionType)

# Test types.GeneratorType
def g():
    yield 1
    yield 2
    yield 3

def test_generator_type():
    assert isinstance(g, types.GeneratorType)
    assert isinstance(g(), types.GeneratorType)

# Test types.LambdaType
def test_lambda_type():
    assert isinstance(lambda: None, types.LambdaType)

# Test types.CodeType
def test_code_type():
    assert isinstance(g.__code__, types.CodeType)
    assert isinstance(test_code_type.__code__, types.CodeType)

# Test types.TracebackType
def test_traceback_type():
    try:
        1/0
    except:
        import sys
        tb = sys.exc_info()[2]
    assert isinstance(tb,
