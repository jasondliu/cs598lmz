import io
# Test io.RawIOBase.
# This test checks that the Python implementation of RawIOBase is
# complete enough to pass the test suite of the io module.

class MockRawIO(io.RawIOBase):
    def __init__(self, read_data):
        self.read_data = read_data
        self.read_pos = 0
        self.write_data = ""
    def read(self, n=-1):
        if self.read_pos == len(self.read_data):
            return ""
        if n == -1 or n >= len(self.read_data):
            s = self.read_data[self.read_pos:]
            self.read_pos = len(self.read_data)
            return s
        s = self.read_data[self.read_pos:self.read_pos+n]
        self.read_pos += n
        return s
    def write(self, s):
        self.write_data += s
        return len(s)
    def seekable(self):
        return False
    def readable(self):
        return True
