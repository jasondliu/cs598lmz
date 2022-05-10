import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)

# Test types.MethodType
assert isinstance(f.__call__, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(abs.__call__, types.BuiltinMethodType)

# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)

# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)

# Test types.CodeType
assert isinstance(f.__code__, types.CodeType)

# Test types.FrameType
def f():
    return types.FrameType
assert isinstance(f(), types.FrameType)

# Test types.TracebackType
try:
    raise Exception
except:
    assert isinstance(sys.exc_info()[2], types.TracebackType)

# Test types.GetSet
