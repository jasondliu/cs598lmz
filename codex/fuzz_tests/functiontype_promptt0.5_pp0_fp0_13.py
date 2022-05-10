import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.LambdaType
assert isinstance(lambda x:x, types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.func_code, types.CodeType)
# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
# Test types.FrameType
assert isinstance(tb.tb_frame, types.FrameType)
# Test types.SliceType
assert isinstance(slice(1,10,2), types.SliceType)
# Test types.XRangeType
assert isinstance(xrange(1,10), types.XRangeType)
# Test types.EllipsisType
