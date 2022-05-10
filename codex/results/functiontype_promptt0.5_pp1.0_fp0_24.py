import types
# Test types.FunctionType()
assert isinstance(types.FunctionType(lambda: None, globals()), types.FunctionType)
# Test types.LambdaType()
assert isinstance(types.LambdaType(lambda: None, globals()), types.LambdaType)

# Test types.GeneratorType()
assert isinstance((lambda: (yield))(), types.GeneratorType)

# Test types.CodeType()
assert isinstance(types.CodeType(0, 0, 0, 0, 0, b"", (), (), (), "", "", 0, b""), types.CodeType)

# Test types.TracebackType()
try:
    raise Exception
except:
    e = sys.exc_info()[2]
    assert isinstance(e, types.TracebackType)

# Test types.FrameType()
assert isinstance(sys._getframe(), types.FrameType)

# Test types.ModuleType()
assert isinstance(sys, types.ModuleType)

# Test types.MethodType()
assert isinstance("".upper, types.MethodType)

