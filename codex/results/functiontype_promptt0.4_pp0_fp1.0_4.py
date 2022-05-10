import types
# Test types.FunctionType
def function_type_test():
    def f():
        pass
    assert type(f) == types.FunctionType

# Test types.LambdaType
def lambda_type_test():
    f = lambda: None
    assert type(f) == types.LambdaType

# Test types.GeneratorType
def generator_type_test():
    def f():
        yield 1
    assert type(f()) == types.GeneratorType

# Test types.CodeType
def code_type_test():
    def f():
        pass
    assert type(f.__code__) == types.CodeType

# Test types.TracebackType
def traceback_type_test():
    try:
        1/0
    except:
        import sys
        tb = sys.exc_info()[2]
        assert type(tb) == types.TracebackType

# Test types.FrameType
def frame_type_test():
    def f():
        import sys
        return sys._getframe()
    assert type(f()) == types.Frame
