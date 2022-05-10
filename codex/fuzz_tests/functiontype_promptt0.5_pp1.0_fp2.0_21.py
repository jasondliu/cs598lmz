import types
# Test types.FunctionType
def f(x):
    return x

assert type(f) is types.FunctionType
assert isinstance(f, types.FunctionType)
assert isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinFunctionType
assert type(len) is types.BuiltinFunctionType
assert isinstance(len, types.BuiltinFunctionType)
assert not isinstance(f, types.BuiltinFunctionType)

# Test types.BuiltinMethodType
assert type([].append) is types.BuiltinMethodType
assert isinstance([].append, types.BuiltinMethodType)
assert not isinstance(f, types.BuiltinMethodType)

# Test types.MethodType
class C(object):
    def f(self):
        pass

assert type(C.f) is types.MethodType
assert isinstance(C.f, types.MethodType)
assert not isinstance(f, types.MethodType)

# Test types.UnboundMethodType
assert type(C.f.__get__(C())) is types.MethodType
assert isinstance(C
