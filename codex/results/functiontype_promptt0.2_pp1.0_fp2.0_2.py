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
class A:
    def f(self):
        pass

assert isinstance(A.f, types.MethodType)
assert not isinstance(A.f, types.FunctionType)

# Test types.BuiltinMethodType
assert isinstance(A.__init__, types.BuiltinMethodType)
assert not isinstance(A.__init__, types.MethodType)

# Test types.LambdaType
assert isinstance((lambda: None), types.LambdaType)
assert not isinstance((lambda: None), types.FunctionType)

# Test types.GeneratorType
assert isinstance((x for x in range(10)), types.GeneratorType)
assert not isinstance((x for x in range(10)), types.Function
