import types
# Test types.FunctionType

def f():
    pass

assert type(f) is types.FunctionType
assert isinstance(f, types.FunctionType)
assert type(f) is types.FunctionType
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType

assert type(len) is types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert type(len) is types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.MethodType

assert type(f.__call__) is types.MethodType
assert isinstance(f.__call__, types.MethodType)
assert type(f.__call__) is types.MethodType
assert isinstance(f.__call__, types.MethodType)

# Test types.UnboundMethodType

assert type(types.UnboundMethodType) is types.TypeType
assert isinstance(types.UnboundMethodType, types.TypeType)
assert type(types.UnboundMethodType) is types.TypeType
assert isinstance
