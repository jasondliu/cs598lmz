import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is not types.BuiltinMethodType
assert type(f) is not types.MethodType
assert type(f) is not types.LambdaType
assert type(f) is not types.UnboundMethodType
# Test types.MethodType
class C:
    def f(self): pass
assert type(C.f) is types.MethodType
assert type(C.f) is not types.BuiltinMethodType
assert type(C.f) is not types.FunctionType
assert type(C.f) is not types.BuiltinFunctionType
assert type(C.f) is not types.LambdaType
assert type(C.f) is not types.UnboundMethodType
# Test types.LambdaType
l = lambda: None
assert type(l) is types.LambdaType
assert type(l) is not types.FunctionType
assert type(l) is not types.BuiltinFunctionType
assert type(l) is not
