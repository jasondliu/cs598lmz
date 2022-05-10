import types
# Test types.FunctionType
def f():
    pass

def g():
    def h():
        pass
    return h

def test_type_FunctionType():
    assert type(f) is types.FunctionType
    assert type(g) is types.FunctionType
    assert type(g()) is types.FunctionType

# Test types.MethodType
def test_type_MethodType():
    class A:
        def m(self):
            pass
    a = A()
    assert type(a.m) is types.MethodType
    assert type(a.m(a)) is types.MethodType

# Test types.BuiltinFunctionType with builtin function
def test_type_BuiltinFunctionType_builtin():
    assert type(len) is types.BuiltinFunctionType

# Test types.BuiltinFunctionType with builtin method
def test_type_BuiltinFunctionType_builtin_method():
    assert type(list.append) is types.BuiltinFunctionType

# Test types.BuiltinFunctionType with builtin method
def test_type_BuiltinFunctionType_builtin_method
