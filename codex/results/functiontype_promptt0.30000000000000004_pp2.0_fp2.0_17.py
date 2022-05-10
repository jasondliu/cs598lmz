import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)

# Test types.MethodType
class C:
    def m(self):
        pass

assert isinstance(C.m, types.MethodType)
assert not isinstance(C.m, types.BuiltinMethodType)

# Test types.BuiltinMethodType
assert isinstance(C.__init__, types.BuiltinMethodType)
assert not isinstance(C.__init__, types.MethodType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)

# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)

# Test types.CoroutineType
async def coro():
    pass

assert isinstance(coro(), types.
