import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)
assert isinstance(f, types.LambdaType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(len, types.FunctionType)
assert not isinstance(len, types.BuiltinMethodType)
assert not isinstance(len, types.MethodType)
assert not isinstance(len, types.LambdaType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
assert isinstance(list.append, types.MethodType)
assert isinstance(list.append, types.FunctionType)
assert isinstance(list.append, types.BuiltinFunctionType)
assert not isinstance(list.append, types.LambdaType)

# Test types.MethodType
class C:
    def
