import _struct

from pytest import raises
from hypothesis import given
from hypothesis.strategies import integers, lists

from . import strategies


@given(strategies.sizes)
def test_size(size):
    result = _struct.calcsize('x' * size)

    assert result == size


@given(lists(integers()))
def test_size_with_format(values):
    format_ = ''.join(map(lambda value: 'B', values))

    result = _struct.calcsize(format_)

    assert result == len(values)


@given(strategies.non_strings)
def test_non_string(non_string):
    with raises(TypeError):
        _struct.calcsize(non_string)
