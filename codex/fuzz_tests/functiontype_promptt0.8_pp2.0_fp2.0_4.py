import types
# Test types.FunctionType
assert isinstance(types.FunctionType, type)
assert issubclass(types.FunctionType, object)
assert issubclass(types.FunctionType, types.TypeType)

# Test types.LambdaType
assert isinstance(types.LambdaType, type)
assert issubclass(types.LambdaType, object)
assert issubclass(types.LambdaType, types.TypeType)

# Test types.CodeType
assert isinstance(types.CodeType, type)
assert issubclass(types.CodeType, object)
assert issubclass(types.CodeType, types.TypeType)

# Test types.TracebackType
assert isinstance(types.TracebackType, type)
assert issubclass(types.TracebackType, object)
assert issubclass(types.TracebackType, types.TypeType)

# Test types.FrameType
assert isinstance(types.FrameType, type)
assert issubclass(types.FrameType, object)
assert issubclass(types.FrameType, types.TypeType)


