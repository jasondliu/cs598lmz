import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert not isinstance(f(), types.FunctionType)
assert not isinstance(None, types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(int, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f(), types.BuiltinFunctionType)
assert not isinstance(None, types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def f(self):
        pass
assert isinstance(C.f, types.MethodType)
assert isinstance(C().f, types.MethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f(), types.MethodType)
assert not isinstance(None, types.MethodType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
