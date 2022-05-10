import types
# Test types.FunctionType
def func(x):
    return x

def test_FunctionType():
    assert type(func) is types.FunctionType

# Test types.BuiltinFunctionType
def test_BuiltinFunctionType():
    assert type(len) is types.BuiltinFunctionType

# Test types.MethodType
def test_MethodType():
    assert type(list.append) is types.MethodType

# Test types.LambdaType
def test_LambdaType():
    assert type(lambda x: x) is types.LambdaType

# Test types.GeneratorType
def test_GeneratorType():
    assert type((x for x in range(10))) is types.GeneratorType

# Test types.CodeType
def test_CodeType():
    assert type(func.__code__) is types.CodeType

# Test types.TracebackType
def test_TracebackType():
    try:
        raise Exception
    except:
        assert type(sys.exc_info()[2]) is types.TracebackType

# Test types.FrameType
