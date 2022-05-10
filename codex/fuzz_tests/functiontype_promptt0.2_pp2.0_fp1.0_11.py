import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)

# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)
assert not isinstance((lambda: None), types.FunctionType)

# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.TracebackType
try:
    1/0
except:
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)

# Test types.FrameType
assert isinstance(sys._getframe(), types.FrameType)

# Test types.GetSetDescriptorType
class C(object
