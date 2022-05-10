import types
# Test types.FunctionType for issue #2360
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)

class C(object):
    def f(self): pass
assert isinstance(C.f, types.MethodType)
assert isinstance(C.f, types.BuiltinMethodType)
assert not isinstance(C.f, types.FunctionType)
assert not isinstance(C.f, types.BuiltinFunctionType)

assert isinstance(C().f, types.MethodType)
assert isinstance(C().f, types.BuiltinMethodType)
assert not isinstance(C().f, types.FunctionType)
assert not isinstance(C().f, types.BuiltinFunctionType)

assert not isinstance(C, types.FunctionType)
assert not isinstance(C, types.BuiltinFunctionType)
assert not isinstance(C, types.MethodType)
assert not isinstance(C, types
