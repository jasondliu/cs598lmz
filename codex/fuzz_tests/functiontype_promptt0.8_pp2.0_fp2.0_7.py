import types
# Test types.FunctionType is a subclass of types.BuiltinFunctionType
assert issubclass(types.FunctionType, types.BuiltinFunctionType)

# Test types.GeneratorType is a subclass of types.FunctionType
assert issubclass(types.GeneratorType, types.FunctionType)

# Test types.GeneratorType is a subclass of types.BuiltinFunctionType
assert issubclass(types.GeneratorType, types.BuiltinFunctionType)

# Test types.CodeType is a subclass of types.ObjectType
assert issubclass(types.CodeType, object)

# Test types.FrameType is a subclass of types.ObjectType
assert issubclass(types.FrameType, object)

# Test types.TracebackType is a subclass of types.ObjectType
assert issubclass(types.TracebackType, object)

# Test types.CellType is a subclass of types.ObjectType
assert issubclass(types.CellType, object)

# Test types.ModuleType is a subclass of types.ObjectType
assert issubclass(types.ModuleType, object)

# Test types.
