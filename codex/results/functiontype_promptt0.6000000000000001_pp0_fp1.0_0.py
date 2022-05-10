import types
# Test types.FunctionType
def test_types_func():
    def f1():
        pass
    def f2(a, b, c):
        pass
    def f3(*args):
        pass
    def f4(**kwargs):
        pass
    def f5(*args, **kwargs):
        pass

    assert isinstance(f1, types.FunctionType)
    assert isinstance(f2, types.FunctionType)
    assert isinstance(f3, types.FunctionType)
    assert isinstance(f4, types.FunctionType)
    assert isinstance(f5, types.FunctionType)

    # Test __code__
    assert isinstance(f1.__code__, types.CodeType)
    assert isinstance(f2.__code__, types.CodeType)
    assert isinstance(f3.__code__, types.CodeType)
    assert isinstance(f4.__code__, types.CodeType)
    assert isinstance(f5.__code__, types.CodeType)

    # Test __defaults__
    assert f1.__defaults
