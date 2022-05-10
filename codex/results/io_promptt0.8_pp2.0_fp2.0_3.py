import io
# Test io.RawIOBase and io.BufferedIOBase for compatibility with the
# implementation of io.IOBase.
class _TestRawIO(io.RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
class _TestBufferedIO(io.BufferedIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
