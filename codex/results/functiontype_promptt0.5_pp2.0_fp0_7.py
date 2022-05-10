import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType

# Test types.MethodType
class C:
    def m(self):
        pass
assert type(C.m) is types.MethodType
assert type(C().m) is types.MethodType

# Test types.UnboundMethodType
assert type(C.m) is types.UnboundMethodType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType

# Test types.GeneratorType
def g():
    yield 1
assert type(g()) is types.GeneratorType

# Test types.CoroutineType
async def c():
    await 1
assert type(c()) is types.CoroutineType

# Test types.MethodWrapperType
assert type(C().__str__) is types.MethodWrapperType

# Test types
