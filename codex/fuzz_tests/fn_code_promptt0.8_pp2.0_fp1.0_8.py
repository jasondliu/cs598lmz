fn = lambda: None
# Test fn.__code__.co_argcount works.
def test_argcount():
    """Test fn.__code__.co_argcount works."""
    assert fn.__code__.co_argcount == 1

# Test fn.__code__.co_cellvars works.
def test_cellvars():
    """Test fn.__code__.co_cellvars works."""
    assert fn.__code__.co_cellvars == ('x',)

# Test fn.__code__.co_consts works.
def test_consts():
    """Test fn.__code__.co_consts works."""
    assert fn.__code__.co_consts == (None,)

# Test fn.__code__.co_filename works.
def test_filename():
    """Test fn.__code__.co_filename works."""
    assert fn.__code__.co_filename == 'test.py'

# Test fn.__code__.co_firstlineno works.
def test_firstlineno():
    """Test fn.__code__.
