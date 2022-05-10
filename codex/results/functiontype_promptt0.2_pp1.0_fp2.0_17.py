import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(1, types.FunctionType)
assert not isinstance(None, types.FunctionType)
assert not isinstance(object, types.FunctionType)
assert not isinstance(type, types.FunctionType)
assert not isinstance(types.FunctionType, types.FunctionType)
assert not isinstance(types, types.FunctionType)
assert not isinstance(types.ModuleType, types.FunctionType)
assert not isinstance(types.TracebackType, types.FunctionType)
assert not isinstance(types.FrameType, types.FunctionType)
assert not isinstance(types.CodeType, types.FunctionType)
assert not isinstance(types.BuiltinFunctionType, types.FunctionType)
assert not isinstance(types.BuiltinMethodType, types.FunctionType)
assert not isinstance(types.MethodType, types.FunctionType)
assert not isinstance(types.UnboundMethodType, types.FunctionType)
assert not isinstance
