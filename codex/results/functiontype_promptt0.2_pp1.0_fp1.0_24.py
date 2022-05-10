import types
# Test types.FunctionType
def f(): pass
assert isinstance(f, types.FunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(len, types.FunctionType)

# Test types.MethodType
class C:
    def m(self): pass
assert isinstance(C.m, types.MethodType)
assert not isinstance(C.m, types.FunctionType)

# Test types.UnboundMethodType
assert isinstance(C.m, types.UnboundMethodType)
assert not isinstance(C.m, types.MethodType)

# Test types.LambdaType
l = lambda: None
assert isinstance(l, types.LambdaType)
assert not isinstance(l, types.FunctionType)

# Test types.GeneratorType
def g(): yield 1
assert isinstance(g(), types.GeneratorType)
assert not isinstance(g(), types.FunctionType)

# Test types.CodeType
assert isinstance
