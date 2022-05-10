import io
# Test io.RawIOBase readinto() return value, when read 0 bytes
# (see https://bugs.python.org/issue25573) and readinto(b"")


class ClassWithReadinto(io.RawIOBase):

    def readinto(self, b):
        return 0


class TestRawIOBase(unittest.TestCase):
    """Tests for io.RawIOBase"""

    def testReadinto(self):
        obj = ClassWithReadinto()
        b = bytearray(10)
        self.assertEqual(obj.readinto(b), 0)
        self.assertEqual(obj.readinto(b), 0)
        b[:] = b"abcd"
        self.assertEqual(obj.readinto(b), 0)
        self.assertEqual(b, b"abcd")
        obj.close()

        self.assertRaises(ValueError, obj.readinto, b"")

    def testInheritFromRawIOBase(self):


        class MyRawIO(io.RawIOBase):

            def readable(self):

