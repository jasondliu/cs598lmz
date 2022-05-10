import io
# Test io.RawIOBase.readinto()
#
# This tests the functionality of the RawIOBase.readinto() method.
#
# This test is a generator, it will yield multiple results.

# The readinto() method is a method of the RawIOBase class.
import io

# Test that the method exists
import types
def test_readinto_exists():
    '''Test that RawIOBase.readinto() exists.'''
    f = io.RawIOBase()
    assert callable(getattr(f, "readinto", None)), "readinto() doesn't exist on RawIOBase."

def test_readinto_ioerror():
    '''Test that RawIOBase.readinto() raises io.UnsupportedOperation.'''
    f = io.RawIOBase()
    try:
        f.readinto(b'')
    except io.UnsupportedOperation:
        pass
    else:
        assert False, "readinto() didn't raise io.UnsupportedOperation"

# Test that the method is a generator
def test_readinto_generator():
    '''Test that RawIOBase
