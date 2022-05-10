import types
# Test types.FunctionType
def f():
    pass
assert type(f) is types.FunctionType
assert type(f) is types.BuiltinFunctionType
assert type(lambda: None) is types.FunctionType
assert type(lambda: None) is types.LambdaType
assert type(int) is types.BuiltinFunctionType
assert type(int) is types.BuiltinFunctionType
assert type(type) is types.BuiltinFunctionType
assert type(type) is types.BuiltinFunctionType
assert type(type(None)) is types.BuiltinFunctionType
assert type(type(None)) is types.BuiltinFunctionType

# Test types.MethodType
class C:
    def f(self):
        pass
assert type(C().f) is types.MethodType
assert type(C().f) is types.BuiltinMethodType
assert type(C.f) is types.BuiltinMethodType
assert type(C.f) is types.MethodType

# Test types.BuiltinMethodType
assert type(list.append) is types.BuiltinMethodType
assert type(list.append) is types.
