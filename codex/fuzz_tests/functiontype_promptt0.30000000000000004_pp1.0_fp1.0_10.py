import types
# Test types.FunctionType

def f(x):
    return x

def g(x):
    return x

class C:
    def m(self, x):
        return x

def test_types():
    assert type(f) is types.FunctionType
    assert type(g) is types.FunctionType
    assert type(C.m) is types.MethodType
    assert type(C.m) is not types.FunctionType
    assert type(C.m) is not types.BuiltinFunctionType
    assert type(C.m) is not types.BuiltinMethodType

def test_types_builtin():
    assert type(len) is types.BuiltinFunctionType
    assert type(len) is not types.FunctionType
    assert type(len) is not types.MethodType
    assert type(len) is not types.BuiltinMethodType

def test_types_method():
    assert type(C().m) is types.MethodType
    assert type(C().m) is not types.FunctionType
    assert type(C().m) is not types.BuiltinFunctionType

