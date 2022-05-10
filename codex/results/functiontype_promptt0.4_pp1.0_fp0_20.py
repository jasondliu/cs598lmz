import types
# Test types.FunctionType
assert isinstance(
    types.FunctionType,
    type
)
assert not isinstance(
    types.FunctionType,
    types.FunctionType
)
assert not isinstance(
    types.FunctionType,
    types.TypeType
)
assert not isinstance(
    types.FunctionType,
    types.BuiltinFunctionType
)
assert not isinstance(
    types.FunctionType,
    types.BuiltinMethodType
)
assert not isinstance(
    types.FunctionType,
    types.MethodType
)
assert not isinstance(
    types.FunctionType,
    types.ModuleType
)
assert not isinstance(
    types.FunctionType,
    types.TracebackType
)
assert not isinstance(
    types.FunctionType,
    types.FrameType
)
assert not isinstance(
    types.FunctionType,
    types.CodeType
)
assert not isinstance(
    types.FunctionType,
    types.GeneratorType
)
assert not isinstance(
    types.FunctionType,
    types.GetSetDescript
