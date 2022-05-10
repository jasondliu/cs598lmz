import io
# Test io.RawIOBase subclass
try:
    import _io
except ImportError:
    pass
else:
    def f(x):
        return x
    class XIO(io.RawIOBase):
        def write(self, x):
            pass
        def writable(self):
            return f(True)
        def seekable(self):
            return f(True)
    x = XIO(None)
    print(x)
    x.name
    print(io.FileIO(__file__))
    print(io.FileIO(__file__, 'r'))
    print(io.FileIO(__file__, 'r+'))
    # io.TextIOBase

    class XText(io.TextIOBase):
        def __init__(self):
            self._fp = io.BytesIO("1")
        def close(self):
            pass
    print(XText())
    # io.TextIOWrapper is built from io.StringIO and io.BufferedReader

    class X:
        def __init__(self, value):
            self._
