import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)

# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)

# Test types.GeneratorType
assert isinstance((x for x in range(3)), types.GeneratorType)

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

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)

# Test types.MethodType
class C:
    def f(
