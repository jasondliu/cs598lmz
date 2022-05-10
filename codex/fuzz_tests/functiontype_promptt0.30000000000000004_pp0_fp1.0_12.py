import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(lambda: None) is types.FunctionType
assert type(lambda x: x) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(abs) is types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.MethodType
class C:
    def f(self): pass
assert type(C.f) is types.MethodType
assert type(C().f) is types.MethodType

# Test types.UnboundMethodType
assert type(C.f) is types.UnboundMethodType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType
assert type(lambda x: x) is types.LambdaType

# Test types.GeneratorType
assert type((x for x in range(10))) is types.GeneratorType

# Test types.CodeType
assert type(f.__code__) is types.CodeType
assert type(C.f.__func__.__code
