import types
# Test types.FunctionType
def test_fn_type():
    def fn(x):
        return x + 1

    assert fn is types.FunctionType


def test_other_type():
    assert 1.0 is float
    assert 1 is int
    assert 1.0 is float, 1 is int
