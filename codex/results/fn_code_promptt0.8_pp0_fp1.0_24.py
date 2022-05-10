fn = lambda: None
# Test fn.__code__ not having the attribute
fn.__code__ = None


def test_convert_object():
    assert convert(2) == 2
    assert convert(3.14) == 3.14
    assert convert('') == ''
    assert convert(None) is None
    assert convert(Convertible()) == 42
    assert convert(fn) is None
    assert convert([1, 2, 3]) == [1, 2, 3]
    assert convert({'foo': 'bar'}) == {'foo': 'bar'}
    assert convert({'foo': 'bar', 'baz': fn, 'quux': Convertible()}) == {'foo': 'bar', 'baz': None, 'quux': 42}


def test_convert_list():
    assert convert([], converter=lambda v: v * 2) == []
    assert convert([1, 2, 3], converter=lambda v: v * 2) == [2, 4, 6]
    assert convert([1, None, 3], converter=lambda v: v * 2) == [2, None, 6]


def test_
