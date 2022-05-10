import io
# Test io.RawIOBase.readinto()
# First, some tests of "raw" type

# Use the helper class defined in io.py
class TestRawIO(io.RawIOBase):

    """Used by test cases."""

    def __init__(self, test_string=""):
        self.read_history = []
        self.readinto_history = []
        self.write_history = []
        self.seq = [ord(c) for c in test_string]

    def readinto(self, buf):
        self.readinto_history.append(buf)
        n = 0
        for i in range(len(buf)):
            if self.seq:
                b = self.seq.pop(0)
                buf[i] = b
                n += 1
            else:
                break
        return n

    def read(self, n=-1):
        b = bytearray(b' ' * n)
        n = self.readinto(b)
        self.read_history.append(n)
