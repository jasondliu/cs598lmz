import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert issubclass(types.FunctionType, object)

# Test types.LambdaType
def test_lambda_type():
    f = lambda: None
    assert isinstance(f, types.LambdaType)
    assert issubclass(types.LambdaType, object)

# Test types.GeneratorType
def test_generator_type():
    def f():
        yield None
    g = f()
    assert isinstance(g, types.GeneratorType)
    assert issubclass(types.GeneratorType, object)

# Test types.CodeType
def test_code_type():
    def f():
        pass
    assert isinstance(f.__code__, types.CodeType)
    assert issubclass(types.CodeType, object)

# Test types.TracebackType
def test_traceback_type():
    try:
        raise Exception
    except:
        import sys
        tb
