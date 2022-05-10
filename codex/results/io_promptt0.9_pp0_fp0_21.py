import io
# Test io.RawIOBase; test incremental writes with os.write()


class TestRawIO(unittest.TestCase):

    def test_write(self):


        class MyBuf(io.RawIOBase):

            def __init__(self):
                self.this = self
                self.buf = bytearray()

            def write(self, b):
                self.buf.extend(b)
                return len(b)

            def readable(self):
                return False

            def writable(self):
                return True

            def seekable(self):
                return False
        a = MyBuf()
        pos = bytearray(b'abcdefghij')
        pos_slc = memoryview(pos)[3:5]
        fpos = pos[3:5]
        slices = [slice(3, 5), slice(2, 6, 2), slice(8, 3, -2), slice(
            -1, -3, -1), slice(3, 10, 2)]
        lengths = [
            len(s) for s in [bytes(pos), bytes
