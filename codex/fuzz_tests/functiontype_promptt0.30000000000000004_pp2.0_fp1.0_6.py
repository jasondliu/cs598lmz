import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.LambdaType
assert isinstance((lambda x: x), types.LambdaType)

# Test types.GeneratorType
def g():
    yield 1

assert isinstance(g(), types.GeneratorType)

# Test types.CoroutineType
async def c():
    pass

assert isinstance(c(), types.CoroutineType)

# Test types.MethodType
class C:
    def m(self):
        pass

assert isinstance(C().m, types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.m, types.UnboundMethodType)

# Test types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)

# Test types.MethodWrapperType
assert isinstance([].__add__, types.MethodWrapperType)

# Test types.
