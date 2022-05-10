import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert isinstance(f, types.FunctionType)

# Test types.LambdaType
def test_lambda_type():
    f = lambda: None
    assert isinstance(f, types.LambdaType)

# Test types.GeneratorType
def test_generator_type():
    def f():
        yield
    g = f()
    assert isinstance(g, types.GeneratorType)

# Test types.CodeType
def test_code_type():
    def f():
        pass
    assert isinstance(f.__code__, types.CodeType)

# Test types.FrameType
def test_frame_type():
    def f():
        import sys
        return sys._getframe()
    assert isinstance(f(), types.FrameType)

# Test types.TracebackType
def test_traceback_type():
    def f():
        import sys
        return sys.exc_info()[2]
    try:
        1/0
    except Zero
