import io
# Test io.RawIOBase's methods.
import io as io
import array
import weakref
import _weakref
import warnings
import _warnings

def test_seek():
    io.BytesIO(b"12345").seek(2) == 2
    io.StringIO("12345").seek(2) == 2

def test_close_fd():
    fd = os.open(os.devnull, os.O_RDONLY)
    file = os.fdopen(fd, 'r')
    file.close()

def test_isatty():
    tty = os.open('/dev/tty', os.O_RDWR)
    file = os.fdopen(tty, 'r+')
    file.isatty() is True
    file.close()

def test_chained_exception():
    try:
        raise TypeError('foo')
    except TypeError as e:
        assert e.args[0] == 'foo'

def test_typeinstancechecks():
    o = object()
    assert isinstance(o, object)
