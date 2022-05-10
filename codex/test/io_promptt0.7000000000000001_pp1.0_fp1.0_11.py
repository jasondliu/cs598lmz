import io
# Test io.RawIOBase.readinto() method.

class ReadintoRawIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def readinto(self, b):
        l = len(b)
        s = self.data[self.pos:self.pos+l]
        b[:len(s)] = s
        self.pos += len(s)
        #print "readinto: pos=%d, len(b)=%d, len(s)=%d" % (self.pos, l, len(s))
        return len(s)

    def readable(self):
        return True

class ReadintoBytesIO(io.BytesIO):
    def readinto(self, b):
        s = self.read(len(b))
        n = len(s)
        b[:n] = s
        return n

def test_readinto():
    b = bytearray(b"hello")
