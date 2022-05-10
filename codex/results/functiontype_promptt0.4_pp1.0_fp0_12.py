import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType) # metaclass hack
# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(f, types.LambdaType)
# Test types.GeneratorType
assert isinstance((lambda: (yield))(), types.GeneratorType)
assert not isinstance((lambda: None)(), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.func_code, types.CodeType)
assert isinstance((lambda: None).func_code, types.CodeType)
# Test types.TracebackType
try:
    raise Exception
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
# Test types.FrameType
assert isinstance(tb.tb_frame, types.FrameType)
# Test types.SliceType

