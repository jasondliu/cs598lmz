import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert isinstance(lambda: None, types.FunctionType)
assert isinstance(int, types.FunctionType)
assert not isinstance(f(), types.FunctionType)

# Test types.BuiltinFunctionType
assert isinstance(int, types.BuiltinFunctionType)
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)
assert not isinstance(f(), types.BuiltinFunctionType)

# Test types.MethodType
class C:
    def f(self): pass
assert isinstance(C.f, types.MethodType)
assert isinstance(C().f, types.MethodType)
assert not isinstance(f, types.MethodType)
assert not isinstance(f(), types.MethodType)

# Test types.UnboundMethodType
assert isinstance(C.f, types.UnboundMethodType)
assert not isinstance(C().f, types.UnboundMethodType)
assert not isinstance(f, types.UnboundMethodType
