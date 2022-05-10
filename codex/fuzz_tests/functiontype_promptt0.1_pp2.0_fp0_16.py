import types
# Test types.FunctionType
def f(): pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(f) is types.BuiltinMethodType
assert type(f) is types.MethodType
assert type(f) is types.LambdaType

# Test types.MethodType
class C:
    def f(self): pass
assert type(C.f) is types.MethodType
assert type(C.f) is types.BuiltinMethodType
assert type(C.f) is types.FunctionType
assert type(C.f) is types.BuiltinFunctionType
assert type(C.f) is types.LambdaType

# Test types.LambdaType
assert type(lambda: None) is types.LambdaType
assert type(lambda: None) is types.FunctionType
assert type(lambda: None) is types.BuiltinFunctionType
assert type(lambda: None) is types.BuiltinMethodType
assert type(lambda: None) is types.MethodType

# Test types.GeneratorType
assert type((lambda: (y
