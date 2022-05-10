import types
# Test types.FunctionType()
def test_FunctionType():
    def tmp(): pass
    def cmp(func):
        assert type(func) == types.FunctionType
        assert isinstance(func, types.FunctionType)
    cmp(tmp)
    cmp(test_FunctionType)
    cmp(cmp)
    cmp(cmp.__call__)
    cmp(cmp.__call__.__get__(cmp))
    cmp(cmp.__call__.__get__(cmp.__call__))
    cmp(cmp.__call__.__get__(cmp.__call__.__get__(cmp)))

    # This should not segfault.
    assert not isinstance(tmp, types.FunctionType)
    assert not isinstance(test_FunctionType, types.FunctionType)
    assert not isinstance(cmp, types.FunctionType)
    assert not isinstance(cmp.__call__, types.FunctionType)
    assert not isinstance(cmp.__call__.__get__(cmp), types.FunctionType)
    assert not isinstance(cmp.__
