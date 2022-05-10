import types
# Test types.FunctionType()
assert isinstance(test_advance_time, types.FunctionType)
# Test types.LambdaType()
assert isinstance(lambda x: x+1, types.LambdaType)
# Test types.MethodType()
assert isinstance(test_advance_time, types.MethodType)
# Test types.BuiltinFunctionType()
assert isinstance(lambda x: x+1, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinFunctionType)
# Test types.GeneratorType()
assert isinstance((x for x in range(3)), types.GeneratorType)
# Test types.TracebackType()
try:
    assert False
except:
    exc_info = sys.exc_info()
    assert isinstance(exc_info[2], types.TracebackType)
# Test types.FrameType()
def test_frame_type():
    assert isinstance(test_frame_type, types.FrameType)
test_frame_type()
# Test types.CodeType()
assert isinstance(test_frame_type.__code
