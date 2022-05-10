import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType

# Test types.LambdaType
assert type(lambda x: x) is types.LambdaType

# Test types.GeneratorType
def f():
    yield
assert type(f()) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType

# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert type(tb) is types.TracebackType

# Test types.FrameType
assert type(sys._getframe()) is types.FrameType

# Test types.SliceType
assert type(slice(1)) is types.SliceType

# Test types.EllipsisType
assert type(Ellipsis) is types.EllipsisType

# Test types.NotImplementedType
assert
