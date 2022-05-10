import types
# Test types.FunctionType
def test_function_type():
    assert isinstance(test_function_type, types.FunctionType)

# Test types.LambdaType
assert isinstance((lambda x: x), types.LambdaType)

# Test types.GeneratorType
assert isinstance((x for x in range(5)), types.GeneratorType)

# Test types.CodeType
assert isinstance(test_function_type.__code__, types.CodeType)

# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.FrameType
assert isinstance(sys._getframe(), types.FrameType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)

# Test types.ModuleType
assert isinstance(types, types.ModuleType)

# Test types.MethodType
class A:

