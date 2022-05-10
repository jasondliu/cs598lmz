import io
# Test io.RawIOBase.readinto()

from test.support import bigmemtest

class ReadIntoTest(unittest.TestCase):

    def test_readinto_wrong_args(self):
        # Issue #22806: readinto() should reject non-writable buffers
        class MyIO(io.RawIOBase):
            def readinto(self, buf):
                return super().readinto(buf)

        with self.assertRaises(TypeError):
            MyIO().readinto(b'1')

    @bigmemtest(size=_4G + 5, memuse=1, dry_run=False)
    def test_readinto_large(self, size):
        # Issue #22806: readinto() should reject non-writable buffers
        class MyIO(io.RawIOBase):
            def readinto(self, buf):
                return super().readinto(buf)

        b = bytearray(size)
        self.assertEqual(MyIO().readinto(b), len(b))


if __name__ == "__main__":
    unittest
