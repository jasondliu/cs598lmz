import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.LambdaType)
# Test types.GeneratorType
def h(): yield
assert isinstance(h(), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
# Test types.FrameType
assert isinstance(h.__code__.co_consts[0], types.FrameType)
# Test types.TracebackType
try:
    1/0
except:
    import sys
    tb = sys.exc_info()[2]
    assert isinstance(tb, types.TracebackType)
# Test types.ModuleType
assert isinstance(types, types.ModuleType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
# Test types.MethodType
class C
