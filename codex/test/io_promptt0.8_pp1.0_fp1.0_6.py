import io
# Test io.RawIOBase

def test_SimpleIOBase():
    class SeqIO(io.RawIOBase):
        def __init__(self, seq):
            self.seq = seq
            self.len = len(seq)
            self.pos = 0

        def readinto(self, b):
            l = len(b)
            result = self.seq[self.pos:self.pos+l]
            n = len(result)
            try:
                b[:n] = result
            except TypeError as err:
                import array
                if not isinstance(b, array.array):
                    raise err
                b[:n] = array.array('b', result)
            self.pos += n
            return n

    # Try a short read
    s = SeqIO(b"hello")
    b = bytearray(3)
    n = s.readinto(b)
    assert n == 3
    assert b == bytearray(b"hel")

    # Try a longer read
    n = s.readinto(b)
    assert n == 2
