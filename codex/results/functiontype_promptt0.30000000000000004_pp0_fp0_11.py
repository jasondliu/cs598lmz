import types
# Test types.FunctionType
def f():
    pass
assert type(f) == types.FunctionType
assert isinstance(f, types.FunctionType)

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert type([].index) == types.BuiltinMethodType
assert isinstance([].index, types.BuiltinMethodType)

# Test types.MethodType
class A:
    def f(self):
        pass
assert type(A.f) == types.MethodType
assert isinstance(A.f, types.MethodType)
assert type(A().f) == types.MethodType
assert isinstance(A().f, types.MethodType)

# Test types.UnboundMethodType
assert type(A.f) == types.UnboundMethodType
assert isinstance(A.f, types.UnboundMethodType)

# Test types.LambdaType
l = lambda: None
assert type(l) == types.LambdaType
assert is
