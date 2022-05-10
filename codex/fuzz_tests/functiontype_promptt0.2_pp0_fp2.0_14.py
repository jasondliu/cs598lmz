import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.LambdaType)

# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C.f, types.FunctionType)
assert isinstance(C.f, types.BuiltinFunctionType)
assert isinstance(C.f, types.BuiltinMethodType)
assert not isinstance(C.f, types.MethodType)
assert not isinstance(C.f, types.LambdaType)

assert isinstance(C().f, types.FunctionType)
assert isinstance(C().f, types.BuiltinFunctionType)
assert isinstance(C().f, types.BuiltinMethodType)
assert isinstance(C().f, types.MethodType)
assert not isinstance(C().f, types.LambdaType)
