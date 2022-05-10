import io
# Test io.RawIOBase
with io.BytesIO(b""):
    pass

# Test io.BufferedIOBase
with io.BytesIO(b"") as bio:
    bio.seek(0)
    bio.tell()

# Test io.IOBase
io.IOBase.seek
io.IOBase.tell

# Test cPickleable bytes-like object
class BytesLike(object):
    def __init__(self, iterable):
        self.buf = b"".join(iterable)
        self.pos = 0

    def read(self, n=-1):
        if n < 0:
            n = len(self.buf) - self.pos
        r = self.buf[self.pos : self.pos + n]
        self.pos += n
        return r

    def tell(self):
        return self.pos

bl = BytesLike([b"abc", b"def"])
