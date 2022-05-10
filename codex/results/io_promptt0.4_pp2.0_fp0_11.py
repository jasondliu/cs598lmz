import io
# Test io.RawIOBase
class TestRawIOBase(unittest.TestCase):
    def test_read(self):
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'abc'
        self.assertEqual(MyRawIO().read(), b'abc')
        self.assertEqual(MyRawIO().read(2), b'ab')
        self.assertEqual(MyRawIO().read(4), b'abc')
        self.assertEqual(MyRawIO().read(0), b'')
        self.assertRaises(TypeError, MyRawIO().read, 'def')
        self.assertRaises(ValueError, MyRawIO().read, -2)
    def test_readall(self):
        class MyRawIO(io.RawIOBase):
            def read(self, n=-1):
                return b'abc'
        self.assertEqual(MyRawIO().readall(), b'abc')
        self.assertEqual(MyRawIO().readall(2), b'ab')
        self
