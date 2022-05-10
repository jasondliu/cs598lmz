import types
# Test types.FunctionType
def f():
    pass

assert type(f) == types.FunctionType
assert type(f) != types.BuiltinFunctionType
assert type(f) != types.BuiltinMethodType

# Test types.BuiltinFunctionType
assert type(len) == types.BuiltinFunctionType
assert type(len) != types.BuiltinMethodType
assert type(len) != types.FunctionType

# Test types.BuiltinMethodType
assert type([].append) == types.BuiltinMethodType
assert type([].append) != types.BuiltinFunctionType
assert type([].append) != types.FunctionType

# Test types.MethodType
class A(object):
    def f(self):
        pass

assert type(A.f) == types.FunctionType
assert type(A.f) != types.MethodType
assert type(A.f) != types.BuiltinFunctionType

assert type(A().f) == types.MethodType
assert type(A().f) != types.FunctionType
assert type(A().f) != types.BuiltinMethodType
