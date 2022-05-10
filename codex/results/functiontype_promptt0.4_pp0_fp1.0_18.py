import types
# Test types.FunctionType

def test_function():
    def f():
        pass
    assert isinstance(f, types.FunctionType)
    assert isinstance(lambda: None, types.FunctionType)
    assert isinstance(test_function, types.FunctionType)

def test_method():
    class C:
        def f(self):
            pass
    assert isinstance(C.f, types.MethodType)
    assert isinstance(C().f, types.MethodType)

def test_builtin_function():
    assert isinstance(len, types.BuiltinFunctionType)
    assert isinstance(test_builtin_function, types.BuiltinFunctionType)

def test_builtin_method():
    assert isinstance([].append, types.BuiltinMethodType)
    assert isinstance([].__add__, types.BuiltinMethodType)
    assert isinstance([].__getitem__, types.BuiltinMethodType)

def test_code():
    assert isinstance(test_code.__code__, types.CodeType)
    assert isinstance(test_code.__
