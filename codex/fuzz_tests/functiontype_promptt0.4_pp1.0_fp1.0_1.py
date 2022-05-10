import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert isinstance(f, types.FunctionType)
assert issubclass(types.FunctionType, object)

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert issubclass(types.BuiltinFunctionType, object)

# Test types.MethodType
class C:
    def f(self): pass
assert type(C.f) is types.MethodType
assert isinstance(C.f, types.MethodType)
assert issubclass(types.MethodType, object)

# Test types.UnboundMethodType
assert type(C.f.__func__) is types.UnboundMethodType
assert isinstance(C.f.__func__, types.UnboundMethodType)
assert issubclass(types.UnboundMethodType, object)

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType
assert isinstance(lambda: None, types.Lamb
