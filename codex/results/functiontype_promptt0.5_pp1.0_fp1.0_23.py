import types
# Test types.FunctionType
assert isinstance(lambda: None, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(print, types.BuiltinFunctionType)
# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
# Test types.CoroutineType
assert isinstance(asyncio.coroutine(lambda: None), types.CoroutineType)
# Test types.MethodType
assert isinstance(print.__call__, types.MethodType)
# Test types.UnboundMethodType
assert isinstance(print, types.UnboundMethodType)
# Test types.BuiltinMethodType
assert isinstance(print.__call__, types.BuiltinMethodType)
# Test types.MethodDescriptorType
assert isinstance(print.__call__, types.MethodDescriptorType)
# Test types.ClassMethodDescriptorType
assert isinstance(print.__call__, types.ClassMethodDescriptorType)
# Test
