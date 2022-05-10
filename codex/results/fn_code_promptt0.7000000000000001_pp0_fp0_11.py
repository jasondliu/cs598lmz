fn = lambda: None
# Test fn.__code__.co_filename is None if fn is not a function.
assert fn.__code__.co_filename is None, "non-function has a co_filename"
# Test fn.__code__.co_filename is None if fn is a lambda.
assert fn.__code__.co_filename is None, "lambda has a co_filename"


@pytest.mark.parametrize("expected", ["<string>", "test_code.py"])
def test_filename(expected):
    """Test that the filename of a function is that of the function's module."""
    import os

    assert test_function.__code__.co_filename == os.path.abspath(expected)


def test_co_flags():
    """Test that the flags of a function are 0."""
    assert test_function.__code__.co_flags == 0


def test_co_argcount():
    """Test that the number of arguments of a function is correct."""
    assert test_function.__code__.co_argcount == 1


def test_co_nlocals
