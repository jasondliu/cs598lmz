import io
# Test io.RawIOBase

# io.RawIOBase.read()

class TestRawIOBaseRead(unittest.TestCase):
    def test_read_0(self):
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'abc'
        self.assertEqual(MyRawIO().read(), b'abc')

    def test_read_1(self):
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'abc'
        self.assertEqual(MyRawIO().read(2), b'ab')

    def test_read_2(self):
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'abc'
        self.assertEqual(MyRawIO().read(42), b'abc')

    def test_read_3(self):
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b''
        self.
