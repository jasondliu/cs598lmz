import types
# Test types.FunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)

# Test types.MethodType
class A(object):
    def f(self):
        pass
assert isinstance(A.f, types.MethodType)
assert isinstance(A.f, types.BuiltinMethodType)
assert not isinstance(A.f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
def f():
    pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)

# Test types.BuiltinMethodType
class A(object):
    def f(self):
        pass
assert isinstance(A.f, types.MethodType)
assert isinstance(A.f, types.BuiltinMethodType)
assert not isinstance(A.f, types.BuiltinFunctionType)

# Test types
