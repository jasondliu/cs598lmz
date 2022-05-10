import types
# Test types.FunctionType

def f(): pass

def g():
    def h(): pass
    return h

class C:
    def m(self): pass

def test_functiontype():
    assert type(f) is types.FunctionType
    assert type(g) is types.FunctionType
    assert type(g()) is types.FunctionType
    assert type(C) is types.ClassType
    assert type(C.m) is types.FunctionType
    assert type(C().m) is types.MethodType
    assert type(C().m) is not types.FunctionType
    assert type(C.m) is not types.MethodType
    assert type(C.m) is not types.UnboundMethodType
    assert type(C().m) is not types.UnboundMethodType
    assert type(C.m) is not types.BuiltinFunctionType
    assert type(C().m) is not types.BuiltinFunctionType
    assert type(C.m) is not types.BuiltinMethodType
    assert type(C().m) is not types.BuiltinMethodType
    assert type(
