import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f, types.UnboundMethodType)
assert not isinstance(f, types.LambdaType)

# Test types.MethodType
class A:
    def f(self): pass
assert isinstance(A.f, types.MethodType)
assert isinstance(A.f, types.BuiltinMethodType)
assert not isinstance(A.f, types.FunctionType)
assert not isinstance(A.f, types.BuiltinFunctionType)
assert not isinstance(A.f, types.UnboundMethodType)
assert not isinstance(A.f, types.LambdaType)

# Test types.UnboundMethodType
assert isinstance(A.f.__func__, types.UnboundMethodType)
assert isinstance(A.f.__func__, types.BuiltinMethodType)

