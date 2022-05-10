import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

# Test types.MethodType
class A(object):
    def f(self):
        pass
a = A()
assert isinstance(a.f, types.MethodType)
assert not isinstance(a.f, types.FunctionType)
assert not isinstance(a.f, types.BuiltinFunctionType)
assert not isinstance(a.f, types.BuiltinMethodType)

# Test types.BuiltinMethodType
assert isinstance(list.append, types.BuiltinMethodType)
assert isinstance(list.append, types.MethodType)
assert not isinstance(list.append, types.FunctionType)
assert not isinstance(list.append, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert isinstance(len
