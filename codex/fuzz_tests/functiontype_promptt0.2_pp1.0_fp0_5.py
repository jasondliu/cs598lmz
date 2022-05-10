import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)

# Test types.MethodType
class C:
    def m(self):
        pass

assert isinstance(C.m, types.MethodType)
assert isinstance(C.m, types.BuiltinMethodType)
assert not isinstance(C.m, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
assert isinstance(list.append, types.MethodType)
assert not isinstance(list.append, types.FunctionType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
assert isinstance(l, types.FunctionType)
assert not isinstance(l, types.BuiltinFunctionType)
assert not isinstance(l, types.BuiltinMethodType)

# Test types.GeneratorType
