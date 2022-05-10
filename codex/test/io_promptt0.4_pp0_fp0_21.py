import io
# Test io.RawIOBase
class MyRawIO(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        super(MyRawIO, self).__init__(*args, **kwargs)
        self.buffer = ''
        self.pos = 0
        self.closed = False
    def readinto(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        if not self.buffer:
            return 0
        n = len(b)
        if len(self.buffer) > n:
            b[:n] = self.buffer[:n]
            self.buffer = self.buffer[n:]
            self.pos += n
            return n
        else:
            n = len(self.buffer)
            b[:n] = self.buffer
            self.buffer = ''
            self.pos += n
            return n
    def write(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        self.buffer += b
