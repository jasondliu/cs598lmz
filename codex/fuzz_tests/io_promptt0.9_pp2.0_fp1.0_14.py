import io
# Test io.RawIOBase.read1.
 
class TestRawIO(io.RawIOBase):
 
    def __init__(self, data):
        self.data = data
        self.offset = 0
 
    def readinto(self, b):
        # print("readinto {} - {}".format(self.pos, self.pos+len(b)))
        n = min(len(self.data) - self.offset, len(b))
        b[:n] = self.data[self.offset:self.offset+n]
        self.offset += n
        return n
 
    def readable(self):
        return True
 
    def seekable(self):
        return False
 
class TestRawIOSeek(TestRawIO):
 
    def __init__(self, data):
        super(TestRawIOSeek, self).__init__(data)
        self.pos = 0
 
    def readinto(self, b):
        # print("readinto {} - {}".format(self.pos, self.pos+len(b)))

