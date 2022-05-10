import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.MethodType)

# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
assert not isinstance(A.f, types.FunctionType)
assert not isinstance(A.f, types.BuiltinFunctionType)

# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)
assert not isinstance((lambda: None), types.FunctionType)
assert not isinstance((lambda: None), types.BuiltinFunctionType)
assert not isinstance((lambda: None), types.MethodType)

# Test types.GeneratorType
assert isinstance((x
