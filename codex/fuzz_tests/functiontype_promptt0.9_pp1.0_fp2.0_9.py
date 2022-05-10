import types
# Test types.FunctionType
def test_typectypes() -> None:
    def foo() -> None:
        pass
    try:
        assert isinstance(foo, types.FunctionType)
    except AssertionError:
        raise AssertionError("types.FunctionType")
    else:
        pass
def test_exception() -> None:
    __counter: int = 0
    try:
        raise AssertionError("Assertion failed")
    except AssertionError as e:
        __counter += 1
    try:
        raise TypeError("Wrong type provided")
    except TypeError as e:
        __counter += 1
    if __counter < 2:
        raise RuntimeError()
def test_builtins() -> None:
    assert isinstance(1, int)
    assert isinstance(1.1, float)
    assert isinstance("s", str)
    assert isinstance(True, bool)
    assert not isinstance(True, int)
    from fractions import Fraction
    assert isinstance(Fraction(2, 3), Fraction)
def test_capitalized_classes
