import types
# Test types.FunctionType
def func(x):
    return x

assert isinstance(func, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.GeneratorType
def gen(x):
    yield x

assert isinstance(gen, types.GeneratorType)
assert isinstance(gen(1), types.GeneratorType)
# Test types.LambdaType
assert isinstance((lambda x: x), types.LambdaType)
# Test types.CodeType
assert isinstance(func.__code__, types.CodeType)
# Test types.FrameType
try:
    1/0
except:
    import sys
    assert isinstance(sys.exc_info()[2], types.FrameType)
# Test types.TracebackType
assert isinstance(sys.exc_info()[2].tb_next, types.TracebackType)
# Test types.SliceType
assert isinstance(slice(1, 2, 3), types.SliceType)
# Test types.EllipsisType
