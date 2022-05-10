import types
# Test types.FunctionType
assert isinstance(lambda: None, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
# Test types.GeneratorType
assert isinstance(x for x in range(0), types.GeneratorType)
# Test types.CoroutineType
async def coro():
    await 1
assert isinstance(coro(), types.CoroutineType)
# Test types.MethodType
def method():
    pass
class C:
    pass
assert isinstance(C().method, types.MethodType)
assert isinstance(C.method, types.MethodType)
# Test types.UnboundMethodType
assert isinstance(C.method, types.UnboundMethodType)
# Test types.MethodWrapperType
assert isinstance(C().method, types.MethodWrapperType)
# Test types.BuiltinMethodType
assert isinstance(C.__new__, types.BuiltinMethodType)
# Test types.ModuleType
