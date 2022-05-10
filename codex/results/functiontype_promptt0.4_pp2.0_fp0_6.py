import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinMethodType)

# Test types.MethodType
class A:
    def g(self): pass
assert not isinstance(A.g, types.FunctionType)
assert not isinstance(A.g, types.BuiltinFunctionType)
assert isinstance(A.g, types.MethodType)
assert not isinstance(A.g, types.BuiltinMethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.FunctionType)
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.MethodType)
assert not isinstance(len, types.BuiltinMethodType)

# Test types.BuiltinMethodType
assert not isinstance(list.append, types.FunctionType)
assert not isinstance(list.append, types.BuiltinFunctionType)
assert isinstance(list
