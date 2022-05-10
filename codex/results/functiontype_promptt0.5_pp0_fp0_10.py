import types
# Test types.FunctionType
def test_function_type():
    assert isinstance(test_function_type, types.FunctionType)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert isinstance(len, types.BuiltinFunctionType)

# Test types.LambdaType
def test_lambda_type():
    assert isinstance(lambda : None, types.LambdaType)

# Test types.GeneratorType
def test_generator_type():
    assert isinstance((x for x in range(10)), types.GeneratorType)

# Test types.CodeType
def test_code_type():
    assert isinstance(test_code_type.__code__, types.CodeType)

# Test types.FrameType
def test_frame_type():
    def inner_test_frame_type():
        assert isinstance(test_frame_type.__code__.co_firstlineno, types.FrameType)
    inner_test_frame_type()

# Test types.TracebackType
def test_traceback_type():

