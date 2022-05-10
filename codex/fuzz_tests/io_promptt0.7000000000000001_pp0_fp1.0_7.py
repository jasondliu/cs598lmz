import io
# Test io.RawIOBase.readinto

import _io

class MockRawIO(io.RawIOBase):
    def __init__(self, read_stack=()):
        self._read_stack = list(read_stack)
        self._read_len = 0
    def readable(self):
        return True
    def readinto(self, buf):
        try:
            data = self._read_stack.pop(0)
        except IndexError:
            data = b''
        n = len(buf)
        self._read_len += n
        if len(data) >= n:
            buf[:n] = data[:n]
            return n
        else:
            buf[:len(data)] = data
            return len(data)
    def read(self, n=-1):
        return super(MockRawIO, self).read(n)
    def readall(self):
        return super(MockRawIO, self).readall()
    def read1(self, n=-1):
        return super(MockRawIO, self).read1(n)
