import types
# Test types.FunctionType, types.LambdaType, types.MethodType and types.BuiltinMethodType
def test_types():
    def f():
        pass
    assert type(f) is types.FunctionType
    assert type(lambda: None) is types.LambdaType
    class C:
        def m(self):
            pass
    assert type(C.m) is types.MethodType
    assert type(C().m) is types.MethodType
    assert type(C.__init__) is types.MethodType
    assert type(C().__init__) is types.MethodType
    assert type(C().__str__) is types.MethodType
    assert type(C().__repr__) is types.MethodType
    assert type(C().__hash__) is types.MethodType
    assert type(C().__eq__) is types.MethodType
    assert type(C().__ne__) is types.MethodType
    assert type(C().__lt__) is types.MethodType
    assert type(C().__le__) is types.MethodType
    assert type(C
