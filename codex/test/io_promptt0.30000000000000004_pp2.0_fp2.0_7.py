import io
# Test io.RawIOBase.readinto()

class MyRawIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.offset = 0
    def readinto(self, b):
        n = len(b)
        if self.offset + n > len(self.data):
            n = len(self.data) - self.offset
        b[:n] = self.data[self.offset:self.offset+n]
        self.offset += n
        return n
    def readable(self):
        return True

def my_raw_io_test():
    # Test readinto()
    r = MyRawIO(b"abc")
    b = bytearray(2)
    n = r.readinto(b)
    assert n == 2 and bytes(b) == b"ab"
    n = r.readinto(b)
    assert n == 1 and bytes(b) == b"cb"
    n = r.readinto(b)
    assert n == 0 and bytes(b) == b"cb"
