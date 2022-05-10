fn = lambda: None
# Test fn.__code__ -> fn code
def test_code():
    assert isinstance(fn.__code__, CodeType)
    assert fn.__code__.co_filename == __file__
    assert fn.__code__.co_firstlineno == co_firstlineno()
    assert fn.__code__.co_name == '<lambda>'

# Test fn.__code__.co_consts -> (None,)
def test_co_consts():
    assert fn.__code__.co_consts == (None,)

# Test fn.__code__.co_args -> ()
def test_co_args():
    assert fn.__code__.co_args == ()

# Test fn.__doc__ -> None
@raises(AttributeError)
def test_doc():
    assert fn.__doc__ == None

# Test fn.__code__.co_nlocals -> 0
def test_co_nlocals():
    assert fn.__code__.co_nlocals == 0

# Test fn.__code__.co_flags -> 67
def
