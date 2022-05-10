fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "fn"
fn.__qualname__ = "fn"

# pylint: disable=unused-variable
# pylint: disable=unused-argument
# pylint: disable=redefined-outer-name

def test_simple_lambda():
    """Test that a simple lambda is parsed correctly."""
    fn = lambda: None
    assert fn.__name__ == "fn"
    assert fn.__qualname__ == "fn"

def test_lambda_as_default_arg():
    """Test that a lambda used as a default argument is parsed correctly."""
    def fn(arg=lambda: None):
        return arg

    assert fn.__name__ == "fn"
    assert fn.__qualname__ == "fn"
    assert fn().__name__ == "fn.<locals>.<lambda>"
    assert fn().__qualname__ == "fn.<locals>.<lambda>"

