import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
assert type(f) != types.BuiltinFunctionType
assert type(f) != types.MethodType
assert type(f) != types.BuiltinMethodType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) != types.FunctionType
assert type(len) != types.MethodType
assert type(len) != types.BuiltinMethodType

# Test types.MethodType
class C:
    def f(self):
        pass

assert type(C.f) == types.MethodType
assert type(C.f) != types.FunctionType
assert type(C.f) != types.BuiltinFunctionType
assert type(C.f) != types.BuiltinMethodType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType
assert type([].append) != types.FunctionType
assert type([].append) != types.BuiltinFunctionType
assert type([].append) != types.MethodType
