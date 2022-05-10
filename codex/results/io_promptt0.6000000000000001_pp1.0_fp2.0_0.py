import io
# Test io.RawIOBase

class RawIOTest(unittest.TestCase):
    def testRawIOBaseInit(self):
        try:
            io.RawIOBase()
        except TypeError:
            pass
        else:
            self.fail('RawIOBase constructor should raise TypeError')

    def testRawIOBaseRead(self):
        class MyRawIO(io.RawIOBase):
            def read(self, n=None):
                return b'x' * n

        r = MyRawIO()
        self.assertEqual(r.read(1), b'x')
        self.assertEqual(r.read(3), b'xxx')
        self.assertEqual(r.read(0), b'')
        self.assertEqual(r.read(1), b'')
        self.assertEqual(r.read(2), b'')
        self.assertEqual(r.read(0), b'')

    def testRawIOBaseReadInto(self):
        class MyRawIO(io.RawIOBase):
            def readinto(self
