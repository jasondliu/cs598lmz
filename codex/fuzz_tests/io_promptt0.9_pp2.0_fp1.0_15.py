import io
# Test io.RawIOBase
class RawTest1(io.RawIOBase):
    def readable(self):
        return False
    def writable(self):
        return False
RawTest1()

# Test io.BufferedIOBase
class BufferedTest1(io.BufferedIOBase):
    def __init__(self):
        self._state = None
    def readable(self):
        return False
    def writable(self):
        return False
    def seekable(self):
        return False
    def read(self, n):
        assert False, 'subclass must implement'
    def peek(self, n):
        assert False, 'subclass must implement'
    def read1(self, n):
        assert False, 'subclass must implement'
    def readinto(self, b):
        assert False, 'subclass must implement'
    def readinto1(self, b):
        assert False, 'subclass must implement'
    def write(self, b):
        assert False, 'subclass must implement'
    def detach(self):
        assert False, "subclass must
