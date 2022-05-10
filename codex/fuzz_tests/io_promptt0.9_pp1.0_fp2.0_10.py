import io
# Test io.RawIOBase, io.BufferedIOBase, io.TextIOBase
assert issubclass(io.RawIOBase, io.IOBase)
assert issubclass(io.BufferedIOBase, io.IOBase)
assert issubclass(io.TextIOBase, io.IOBase)
# Test io.BlockingIOError
try:
    b = io.BlockingIOError(42, "message", 10)
    assert b.errno == 42
    assert b.strerror == "message"
    assert b.characters_written == 10
except AttributeError:
    pass
# Test exception hierarchy
try:
    i = isinstance
    assert i(IOError(), BaseException)
    assert i(IOError(), Exception)
    assert i(IOError(), StandardError)

    assert i(EnvironmentError, BaseException)
    assert i(EnvironmentError, Exception)
    assert i(EnvironmentError, StandardError)
    assert i(EnvironmentError, EnvironmentError)

    assert i(OSError, BaseException)
    assert i(OSError, Exception)
    assert i(OSError, Standard
