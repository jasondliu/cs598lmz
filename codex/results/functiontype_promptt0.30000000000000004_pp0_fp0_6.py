import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)

# Test types.BuiltinMethodType
assert isinstance(len, types.BuiltinMethodType)
assert not isinstance(len, types.MethodType)

# Test types.MethodType
class C(object):
    def f(self): pass
assert isinstance(C.f, types.MethodType)
assert not isinstance(C.f, types.BuiltinMethodType)

# Test types.UnboundMethodType
assert isinstance(C.f, types.UnboundMethodType)
assert not isinstance(C.f, types.MethodType)

# Test types.LambdaType
assert isinstance(lambda: None, types.LambdaType)
assert not isinstance(lambda: None, types.FunctionType)

# Test types.GeneratorType
assert isinstance((
