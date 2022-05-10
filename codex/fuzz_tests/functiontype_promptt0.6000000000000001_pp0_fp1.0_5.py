import types
# Test types.FunctionType
def test_types_FunctionType():
    assert types.FunctionType is type(test_types_FunctionType)

# Test types.BuiltinFunctionType
def test_types_BuiltinFunctionType():
    assert types.BuiltinFunctionType is type(len)

# Test types.LambdaType
def test_types_LambdaType():
    assert types.LambdaType is type(lambda: None)

# Test types.GeneratorType
def test_types_GeneratorType():
    assert types.GeneratorType is type((i for i in range(1)))

# Test types.CodeType
import dis
def test_types_CodeType():
    assert types.CodeType is type(dis.dis.__code__)

# Test types.FrameType
import sys
def test_types_FrameType():
    assert types.FrameType is type(sys._getframe())

# Test types.TracebackType
def test_types_TracebackType():
    try:
        raise Exception()
    except Exception as e:
        assert types.TracebackType
