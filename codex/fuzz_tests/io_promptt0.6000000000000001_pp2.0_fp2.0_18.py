import io
# Test io.RawIOBase

class MyRawIO(io.RawIOBase):
    def read(self, n=-1):
        if n >= 0:
            return b'x' * n
        else:
            return b'xyz'

    def write(self, b):
        assert 0, "shouldn't get here"

    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        if whence == 1:
            pos += self.tell()
        elif whence == 2:
            pos += 3
        assert 0 <= pos <= 3
        self.pos = pos

    def tell(self):
        return self.pos

    def readable(self):
        return True

    def writable(self):
        return False

    def readinto(self, b):
        data = self.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array) or b.typecode != 'b':

