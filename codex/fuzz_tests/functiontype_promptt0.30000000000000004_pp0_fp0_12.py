import types
# Test types.FunctionType
def test_function_type():
    def func():
        pass
    assert isinstance(func, types.FunctionType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(len, types.BuiltinFunctionType)

# Test types.LambdaType
def test_lambda_type():
    f = lambda x: x
    assert isinstance(f, types.LambdaType)

# Test types.GeneratorType
def test_generator_type():
    def gen():
        yield 1
    assert isinstance(gen(), types.GeneratorType)

# Test types.CodeType
def test_code_type():
    def func():
        pass
    assert isinstance(func.__code__, types.CodeType)

# Test types.TracebackType
def test_traceback_type():
    try:
        1 / 0
    except:
        assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.FrameType
def test_frame
