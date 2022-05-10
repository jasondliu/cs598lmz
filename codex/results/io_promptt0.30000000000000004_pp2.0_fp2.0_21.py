import io
# Test io.RawIOBase

import io

class TestRawIO(io.RawIOBase):

    def __init__(self, test_string):
        self.string = test_string
        self.read_sofar = 0

    def readinto(self, b):
        length = len(b)
        data = self.string[self.read_sofar:self.read_sofar+length]
        bytes_read = len(data)
        b[:bytes_read] = data
        self.read_sofar += bytes_read
        return bytes_read

    def write(self, b):
        self.read_sofar += len(b)
        return len(b)

def test_rawio_readinto():
    r = TestRawIO("abcdefghijklmnop")
    b = bytearray(10)
    n = r.readinto(b)
    assert n == 10
    assert b == bytearray(b"abcdefghij")
    n = r.readinto(b)
    assert n == 6
    assert b[:6] == bytear
