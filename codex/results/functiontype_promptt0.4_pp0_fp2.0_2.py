import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
# Test types.LambdaType
g = lambda x: x

assert isinstance(g, types.LambdaType)
# Test types.GeneratorType
def h():
    yield 1

assert isinstance(h(), types.GeneratorType)
# Test types.CodeType
assert isinstance(h.__code__, types.CodeType)
# Test types.TracebackType
try:
    raise ValueError
except:
    tb = sys.exc_info()[2]

assert isinstance(tb, types.TracebackType)
# Test types.FrameType
assert isinstance(tb.tb_frame, types.FrameType)
# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(abs, types.BuiltinMethodType)
# Test types.ModuleType
assert isinstance(types, types.ModuleType)
# Test types.MethodType
assert isinstance
