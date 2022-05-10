import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert isinstance(int, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert isinstance(int.__add__, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert isinstance(f.__call__, types.MethodType)
assert not isinstance(f, types.UnboundMethodType)
assert isinstance(f.__call__, types.UnboundMethodType)
assert not isinstance(f, types.LambdaType)
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(f, types.GeneratorType)
assert isinstance((x for x in range(10)), types.GeneratorType)
assert not isinstance(f, types.CodeType)
assert isinstance(f.__code__,
