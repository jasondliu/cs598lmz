import types
# Test types.FunctionType
def test_function_type():
    def f():
        pass
    assert type(f) is types.FunctionType
    assert type(lambda x: x) is types.FunctionType
    assert type(test_function_type) is types.FunctionType
    assert type(test_function_type.__call__) is types.FunctionType
    class C(object):
        def m(self):
            pass
    assert type(C.m) is types.FunctionType
    assert type(C.m.__get__(C())) is types.FunctionType
    assert type(C.m.__get__(C()).__call__) is types.FunctionType

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert type(len) is types.BuiltinFunctionType
    assert type(len.__call__) is types.BuiltinFunctionType
    assert type(test_builtin_function_type) is types.BuiltinFunctionType
    assert type(test_builtin_function_type.__call__) is types.BuiltinFunctionType
