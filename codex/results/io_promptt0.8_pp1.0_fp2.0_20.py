import io
# Test io.RawIOBase by simulating a stream of characters
import random
import string

READ_SIZE = 10

class RandomBytes(io.RawIOBase):
    def __init__(self, length):
        self.length = length

    def seekable(self):
        return True

    def readable(self):
        return True

    def readinto(self, b):
        if len(b) > self.length:
            b[:self.length] = self._readall()
            return self.length
        n = len(b)
        b[:n] = self._readall()
        return n

    def _readall(self):
        n = self.length
        self.length = 0
        return [ random.choice(string.ascii_letters) for _ in xrange(n) ]

rb = RandomBytes(random.randrange(1, READ_SIZE))
print(rb.readall())
