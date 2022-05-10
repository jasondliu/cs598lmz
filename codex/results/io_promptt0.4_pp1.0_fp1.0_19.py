import io
# Test io.RawIOBase

# Test RawIOBase.read()

class TestRawIO(io.RawIOBase):

    def __init__(self, test_string):
        self.string_len = len(test_string)
        self.read_len = 0
        self.test_string = test_string

    def read(self, n=-1):
        if self.read_len == self.string_len:
            return b''
        if n < 0 or n > self.string_len - self.read_len:
            r = self.test_string[self.read_len:]
            self.read_len = self.string_len
            return r
        r = self.test_string[self.read_len:self.read_len+n]
        self.read_len += n
        return r

    def readable(self):
        return True

class TestRawIOWithoutRead(io.RawIOBase):
    def readable(self):
        return True

class TestRawIOWithReadinto(io.RawIOBase):

    def __init__(self, test
