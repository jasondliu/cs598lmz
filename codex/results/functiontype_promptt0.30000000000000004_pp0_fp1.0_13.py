import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
# Test types.LambdaType
g = lambda x: x
assert isinstance(g, types.LambdaType)
# Test types.GeneratorType
def h(): yield
assert isinstance(h(), types.GeneratorType)
# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)
# Test types.FrameType
assert isinstance(h.__code__.__closure__[0].cell_contents, types.FrameType)
# Test types.TracebackType
try:
    raise Exception
except:
    import sys
    assert isinstance(sys.exc_info()[2], types.TracebackType)
# Test types.ModuleType
import types
assert isinstance(types, types.ModuleType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
# Test types.MethodType
class C:
