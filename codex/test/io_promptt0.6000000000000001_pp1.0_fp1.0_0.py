import io
# Test io.RawIOBase.readall()

class TestRawIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0

    def read(self, size=-1):
        if size == -1:
            size = len(self.data) - self.pos
        if size == 0:
            return ''
        self.pos += size
        return self.data[self.pos - size:self.pos]

    def readable(self):
        return True

# Read into a buffer
buf = bytearray(10)
r = TestRawIO(b'abcdefg')
