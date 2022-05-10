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
