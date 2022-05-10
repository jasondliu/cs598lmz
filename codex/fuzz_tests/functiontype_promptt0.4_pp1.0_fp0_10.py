import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert not isinstance(None, types.FunctionType)
# Test types.BuiltinFunctionType
assert isinstance(abs, types.BuiltinFunctionType)
assert isinstance(min, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(None, types.BuiltinFunctionType)
# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
assert isinstance(tuple.count, types.BuiltinMethodType)
assert not isinstance(None, types.BuiltinMethodType)
# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C.f, types.MethodType)
assert isinstance(C().f, types.MethodType)
assert not isinstance(None, types.MethodType)
# Test types.LambdaType
assert isinstance(lambda: None, types.Lamb
