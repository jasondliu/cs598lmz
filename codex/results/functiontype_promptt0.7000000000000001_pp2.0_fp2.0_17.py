import types
# Test types.FunctionType
try:
    import _testcapi
except ImportError:
    _testcapi = None

def test_function_type():
    def f(): pass
    assert type(f) is types.FunctionType
    assert isinstance(f, types.FunctionType)
    class C:
        def f(self): pass
    assert type(C.f) is types.FunctionType
    assert isinstance(C.f, types.FunctionType)

    class D(C):
        def g(self): pass
    assert type(D.f) is types.FunctionType
    assert isinstance(D.f, types.FunctionType)
    assert type(D.g) is types.FunctionType
    assert isinstance(D.g, types.FunctionType)

    if _testcapi is not None:
        assert type(_testcapi.testfunc) is types.FunctionType
        assert isinstance(_testcapi.testfunc, types.FunctionType)

    assert not isinstance(f, types.BuiltinFunctionType)
    assert not isinstance(C.f, types.Builtin
