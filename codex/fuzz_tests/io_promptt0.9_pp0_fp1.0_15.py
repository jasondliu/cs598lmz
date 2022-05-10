import io
# Test io.RawIOBase

def test_implicit_close_when_in_destructor_of_unclosed_stream():
    class DontCloseMe(io.RawIOBase):
        def read(self, size=-1):
            return b""

    try:
        DontCloseMe()
    except BaseException:
        pass

# Test io.BufferedIOBase

# Test io.TextIOBase

def test_newline_attribute():
    r = io.StringIO("\r\n")
    assert r.newlines == '\r\n'
    r = io.StringIO('test\r\n\r\n')
    assert r.newlines == '\r\n'
    # 'x' is a temporary variable, just to make sure it's not returned
    r._read(1)
    x = r.newlines
    r._read(2)
    assert x == r.newlines == '\r\n'
    r._read(30)
    assert r.newlines == '\r\n\r\n'
    r = io.
