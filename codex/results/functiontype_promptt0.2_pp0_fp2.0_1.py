import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)
assert isinstance(f, types.LambdaType)
assert isinstance(f, types.UnboundMethodType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
assert isinstance(abs, types.FunctionType)
assert isinstance(abs, types.BuiltinMethodType)
assert isinstance(abs, types.MethodType)
assert isinstance(abs, types.LambdaType)
assert isinstance(abs, types.UnboundMethodType)

# Test types.BuiltinMethodType
assert isinstance(abs, types.BuiltinMethodType)
assert isinstance(abs, types.FunctionType)
assert isinstance(abs, types.BuiltinFunctionType)
assert isinstance(abs, types.MethodType)
assert isinstance(abs, types.LambdaType)
assert isinstance
