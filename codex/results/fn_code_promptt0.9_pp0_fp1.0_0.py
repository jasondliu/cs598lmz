fn = lambda: None
# Test fn.__code__ attribute raises when fn is a built-in.
with pytest.raises(AttributeError):
    badfn.__code__


def test_enumerator_values():
    assert enumerate([(1, 2)])[0] == (0, (1, 2))
    assert list(enumerate([(1, 2)])) == [(0, (1, 2))]


def test_print():
    mystdout = io.StringIO()
    print('hello', file=mystdout)
    assert mystdout.getvalue() == 'hello\n'


def test_nested_tuple_unpacking_in_for():
    x = [(1, (2, 3)), (4, (5, 6))]
    y = list(itertools.chain.from_iterable(x))
    assert y == [1, (2, 3), 4, (5, 6)]


@pytest.mark.parametrize(
    'concurrency', [asyncio.get_event_loop().set_debug])
@pytest.mark.skip
