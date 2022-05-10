import io
# Test io.RawIOBase
class RawIOBaseTest(unittest.TestCase):
    class IOTest(io.RawIOBase):
        def readable(self):
            return True
        def writable(self):
            return True
        def seekable(self):
            return True
    def setUp(self):
        self.i = RawIOBaseTest.IOTest()
    def tearDown(self):
        self.i.close()
    def test_readinto(self):
        b = bytearray(1)
        self.assertRaises(TypeError, self.i.readinto, b)
        self.assertRaises(TypeError, self.i.readinto, object())
        self.assertIs(self.i.readinto(b), None)
        b = bytearray(0)
        self.assertIs(self.i.readinto(b), 0)
    def test_seek(self):
        self.assertRaises(TypeError, self.i.seek)
        self.assertRaises(TypeError, self.i.seek, 0, 1
