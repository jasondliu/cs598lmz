import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.LambdaType)

# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
assert not isinstance(abs, types.FunctionType)
assert not isinstance(abs, types.MethodType)
assert not isinstance(abs, types.BuiltinMethodType)
assert not isinstance(abs, types.LambdaType)

# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C.f, types.MethodType)
assert not isinstance(C.f, types.FunctionType)
assert not isinstance(C.f, types.BuiltinFunctionType)
assert not isinstance(C.f, types.BuiltinMethodType)
assert not isinstance(C.f, types
