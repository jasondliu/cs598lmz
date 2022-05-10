import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)
assert isinstance(f, types.LambdaType)

# Test types.MethodType
class A:
    def f(self):
        pass

assert isinstance(A.f, types.FunctionType)
assert isinstance(A.f, types.BuiltinFunctionType)
assert isinstance(A.f, types.BuiltinMethodType)
assert isinstance(A.f, types.MethodType)
assert isinstance(A.f, types.LambdaType)

# Test types.LambdaType
g = lambda: None
assert isinstance(g, types.FunctionType)
assert isinstance(g, types.BuiltinFunctionType)
assert isinstance(g, types.BuiltinMethodType)
assert isinstance(g, types.MethodType)
assert isinstance(g, types.LambdaType)
