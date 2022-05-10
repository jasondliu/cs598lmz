fn = lambda: None
# Test fn.__code__.co_varnames
@pytest.mark.parametrize("test_input,expected", [
    (fn, []),
    (my_add, ['a', 'b']),
])
def test_co_varnames(test_input, expected):
    assert test_input.__code__.co_varnames == expected


# Test fn.__code__.co_filename
@pytest.mark.parametrize("test_input,expected", [
    (fn, '<string>'),
    (my_add, '<string>'),
    (pytest, 'fixtures.py'),
])
def test_co_filename(test_input, expected):
    assert test_input.__code__.co_filename == expected


# Test fn.__code__.co_argcount
@pytest.mark.parametrize("test_input,expected", [
    (fn, 0),
    (my_add, 2),
    (pytest, 0)
])
def test_co_argcount(test_input, expected):

