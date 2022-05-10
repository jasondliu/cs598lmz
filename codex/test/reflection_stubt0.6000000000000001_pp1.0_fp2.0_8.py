fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code


def test_code():
    """Test code object."""
    assert fn.__code__
    assert isinstance(fn.__code__, types.CodeType)


def test_code_name():
    """Test code object name."""
    assert fn.__code__.co_name == '<lambda>'


def test_code_filename():
    """Test code object filename."""
    assert fn.__code__.co_filename == '<unknown>'


def test_code_firstlineno():
    """Test code object firstlineno."""
    assert fn.__code__.co_firstlineno == 0


def test_code_lnotab():
    """Test code object lnotab."""
    assert fn.__code__.co_lnotab == b''


def test_code_stacksize():
    """Test code object stacksize."""
    assert fn.__code__.co_stacksize == 2


def test_code_flags():
    """Test code object flags."""
