fn = lambda: None
# Test fn.__code__.co_filename
def test_filename():
    assert fn.__code__.co_filename == '<stdin>'

# Test fn.__code__.co_firstlineno
def test_firstlineno():
    assert fn.__code__.co_firstlineno == 1

# Test fn.__code__.co_flags
def test_flags():
    assert fn.__code__.co_flags == 0

# Test fn.__code__.co_lnotab
def test_lnotab():
    assert fn.__code__.co_lnotab == b'\x00\x01\x0c\x01'

# Test fn.__code__.co_name
def test_name():
    assert fn.__code__.co_name == '<lambda>'

# Test fn.__code__.co_names
def test_names():
    assert fn.__code__.co_names == ()

# Test fn.__code__.co_nlocals
def test_nlocals():
    assert fn.__code
