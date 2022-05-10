import io
# Test io.RawIOBase().readinto()


class MyRawIO(io.RawIOBase):

    def __init__(self, bufsize):
        self._bufsize = bufsize
        self._buf = bytearray(bufsize)
        self._offset = 1
        self._length = bufsize - 2

    def readinto(self, bytestr):
        readlen = min(len(bytestr), self._length)
        until = self._offset + readlen
        bytestr[:readlen] = self._buf[self._offset:until]
        self._offset = until
        self._length = self._length - readlen
        return readlen

    def readable(self):
        return True


def test_readinto():
    record = list(range(10))
    with io.BytesIO() as u:
        with MyRawIO(10 + 1) as f:
            io.BufferedRWPair(u, f, 1)
            u.write(b'y')
            f.seek(10 - 2)
            buf = bytearray(3)

