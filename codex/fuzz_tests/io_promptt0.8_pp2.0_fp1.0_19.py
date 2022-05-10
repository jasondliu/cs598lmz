import io
# Test io.RawIOBase with a read-only stream
class MyRawIO(io.RawIOBase):
    def __init__(self, raw):
        self._raw = raw

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast('B')
        while n > 0:
            try:
                buf = self._raw.read(n)
            except OSError as e:
                if e.errno == EINTR:
                    continue
                else:
                    raise
            if not buf:
                return len(b) - n
            view[:len(buf)] = buf
            n -= len(buf)
        return len(b)

    def write(self, b):
        raise io.UnsupportedOperation("read-only stream")

    def seek(self, pos, whence=io.SEEK_SET):
        return self._raw.seek(pos, whence)

    def
