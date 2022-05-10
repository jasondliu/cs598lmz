import types
# Test types.FunctionType
def f():
    pass

assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)
assert isinstance(f, types.BuiltinMethodType)
assert isinstance(f, types.MethodType)
assert isinstance(f, types.LambdaType)
assert isinstance(f, types.UnboundMethodType)

# Test types.MethodType
class C:
    def f(self):
        pass

assert isinstance(C.f, types.FunctionType)
assert isinstance(C.f, types.BuiltinFunctionType)
assert isinstance(C.f, types.BuiltinMethodType)
assert isinstance(C.f, types.MethodType)
assert isinstance(C.f, types.LambdaType)
assert isinstance(C.f, types.UnboundMethodType)

# Test types.UnboundMethodType
assert isinstance(C.f, types.FunctionType)
assert isinstance(C.f, types.BuiltinFunctionType)
assert isinstance(C.f, types.Built
