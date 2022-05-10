import io
# Test io.RawIOBase

# Test RawIOBase.read()

class TestRawIO(io.RawIOBase):
    def __init__(self, test_string):
        self.string_len = len(test_string)
        self.read_len = 0
        self.test_string = test_string

    def read(self, n=-1):
        if n == -1:
            n = self.string_len
        if self.read_len + n > self.string_len:
            n = self.string_len - self.read_len
        result = self.test_string[self.read_len:self.read_len+n]
        self.read_len += n
        return result

    def readable(self):
        return True

    def seekable(self):
        return False

    def writable(self):
        return False

def test_read():
    rawio = TestRawIO(b"1234567890")
    assert rawio.read() == b"1234567890"
    assert rawio.read() == b""
