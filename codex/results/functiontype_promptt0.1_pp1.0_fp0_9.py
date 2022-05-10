import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.BuiltinMethodType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)
assert not isinstance(len, types.MethodType)
assert not isinstance(len, types.BuiltinMethodType)

# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C.f, types.MethodType)
assert not isinstance(C.f, types.FunctionType)
assert not isinstance(C.f, types.BuiltinFunctionType)
assert not isinstance(C.f, types.BuiltinMethodType)

# Test types.BuiltinMethodType
assert isinstance(C.__init__, types.BuiltinMethodType)
assert not isinstance(C.__init__, types
