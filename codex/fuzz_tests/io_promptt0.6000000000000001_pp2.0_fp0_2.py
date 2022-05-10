import io
# Test io.RawIOBase.seek()

class MyIO(io.RawIOBase):
    def __init__(self):
        self.pos = 0

    def readinto(self, b):
        n = len(b)
        if self.pos + n > 10:
            n = 10 - self.pos
        for i in range(n):
            b[i] = self.pos + i + 65
        self.pos += n
        return n

    def seekable(self):
        return True

    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.pos = pos
        elif whence == io.SEEK_CUR:
            self.pos += pos
        elif whence == io.SEEK_END:
            self.pos = 10 + pos
        else:
            raise ValueError("whence value not supported")
        return self.pos

import sys
if sys.flags.optimize < 1:
    i = MyIO()
    print(i.seek(5))
    print(i.
