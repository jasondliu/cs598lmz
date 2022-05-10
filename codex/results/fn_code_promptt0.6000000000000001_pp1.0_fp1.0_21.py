fn = lambda: None
# Test fn.__code__ exists since it is not defined in Python 3.0 and 3.1
if hasattr(fn, '__code__'):
    fn.__code__ = type(fn.__code__)(
        0, 0, 0, 0, b'', b'', (), (), (),
        b'', b'', 0, b'')
    assert fn.__code__.co_filename == ''


def test_code_no_args():
    """Test that code objects can be created without arguments."""
    code = type(lambda: 0)
    # This should not raise an exception.
    code(0, 0, 0, 0, b'', b'', (), (), (),
         b'', b'', 0, b'')


def test_code_bad_args():
    """Test that code objects can not be created with bad arguments."""
    code = type(lambda: 0)
    with pytest.raises(TypeError):
        code(0, 0, 0, 0, b'', b'', (), (), (),
             b'', b'', 0, b'', 0)


