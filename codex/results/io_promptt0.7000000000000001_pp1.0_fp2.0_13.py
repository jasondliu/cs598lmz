import io
# Test io.RawIOBase
class TestRawIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.readsofar = 0
        self.closed = False

    def close(self):
        if not self.closed:
            self.closed = True

    def readable(self):
        return True

    def readinto(self, buf):
        if len(buf) == 0:
            return 0
        if self.readsofar == len(self.data):
            return 0
        buflen = len(buf)
        readlen = min(len(self.data) - self.readsofar, buflen)
        buf[0:readlen] = self.data[self.readsofar:self.readsofar+readlen]
        self.readsofar += readlen
        return readlen

    def writable(self):
        return False

    def seekable(self):
        return False

def test_main():
    data  = b"".join([bytes([i%256]) for i in range(65536)])
    stream = Test
