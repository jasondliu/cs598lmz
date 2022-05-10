import types
# Test types.FunctionType
def f():
    pass

assert type(f) is types.FunctionType
assert type(f) is types.FunctionType
assert type(f) is types.FunctionType

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType

# Test types.MethodType
class A:
    def m(self):
        pass

assert type(A.m) is types.MethodType
assert type(A.m) is types.MethodType
assert type(A.m) is types.MethodType

# Test types.BuiltinMethodType
assert type(list.append) is types.BuiltinMethodType
assert type(list.append) is types.BuiltinMethodType
assert type(list.append) is types.BuiltinMethodType

# Test types.LambdaType
assert type(lambda x: x) is types.LambdaType
assert type(lambda x: x) is types.LambdaType
assert type(lambda x
