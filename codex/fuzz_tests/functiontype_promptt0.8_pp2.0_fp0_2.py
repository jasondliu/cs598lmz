import types
# Test types.FunctionType
assert isinstance(lambda x: x, types.FunctionType)
# Test types.ClassType
assert isinstance(object, types.ClassType)
# Test types.NoneType
assert isinstance(None, types.NoneType)
# Test types.InstanceType
assert isinstance(int, types.ClassType)
assert isinstance(int(), types.InstanceType)
# Test types.LambdaType
f = lambda: None
assert isinstance(f, types.LambdaType)
# Test types.GeneratorType
g = iter(range(10))
assert isinstance(g, types.GeneratorType)
# Test types.UnboundMethodType
assert isinstance(object.__init__, types.UnboundMethodType)
# Test types.MethodType
assert isinstance(object().__init__, types.MethodType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
# Test types.ModuleType
assert isinstance(types, types
