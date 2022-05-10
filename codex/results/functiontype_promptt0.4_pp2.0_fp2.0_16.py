import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert isinstance(test_function_type, types.FunctionType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(len, types.BuiltinFunctionType)

# Test types.LambdaType
def test_lambda_type():
    assert isinstance(lambda: None, types.LambdaType)

# Test types.GeneratorType
def test_generator_type():
    def f():
        yield None
    assert isinstance(f(), types.GeneratorType)

# Test types.CodeType
def test_code_type():
    def f():
        pass
    assert isinstance(f.__code__, types.CodeType)

# Test types.TracebackType
def test_traceback_type():
    try:
        raise Exception
    except Exception:
        tb = sys.exc_info()[2]
        assert isinstance(tb, types
