fn = lambda: None
# Test fn.__code__ for Python 2.x and fn.__closure__ for Python 3.x
# Also, fn.func_closure will contain None if closure wasn't used.

from pytest import raises as pytest_raises

from ..decorators.deprecated import deprecated, deprecated_parameter
from ..exceptions import AstropyDeprecationWarning


def test_deprecated_function_is_called():
    @deprecated('0.7', alternative='fn2')
    def fn():
        return 'a'

    assert fn() == 'a'


def test_deprecated_function_without_alternative_message():
    @deprecated('1.0')
    def fn():
        return 'a'

    with pytest_raises(AstropyDeprecationWarning) as exc:
        assert fn() == 'a'
    assert "The function 'fn' is deprecated" in str(exc.value)


def test_deprecated_function_with_alternative_message():
    @deprecated('1.0', alternative='fn2')
    def fn():
        return 'a'

   
