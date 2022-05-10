import types
# Test types.FunctionType
assert isinstance(a, types.FunctionType)
# Test types.LambdaType
assert isinstance(lambda x: x, types.LambdaType)
# Test types.GeneratorType
assert isinstance(gen(), types.GeneratorType)
# Test types.BuiltinFunctionType
assert isinstance(int, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(int.__add__, types.BuiltinMethodType)
# Test types.MethodType
assert isinstance(TestClass.test, types.MethodType)
# Test types.UnboundMethodType
assert isinstance(TestClass.test, types.UnboundMethodType)

# Test types.ClassType
assert isinstance(TestClass, types.ClassType)
# Test types.InstanceType
assert isinstance(TestClass(), types.InstanceType)
# Test types.FloatType
assert isinstance(1.0, types.FloatType)
# Test types.IntType
assert isinstance(1, types.IntType)
# Test types.LongType
assert isinstance(100000000000000000000, types
