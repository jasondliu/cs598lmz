import io
# Test io.RawIOBase.readinto

import _io

READ_SUPPORT = hasattr(_io.RawIOBase, 'readinto')


class TestRawIOBase(unittest.TestCase):

    def test_readinto(self):
        if not READ_SUPPORT:
            self.skipTest("RawIOBase.readinto not implemented")
        io.BytesIO(b"abc").readinto(bytearray(b"xyz"))
        self.assertEqual(b"abc", bytearray(b"xyz"))

    def test_readinto_array(self):
        if not READ_SUPPORT:
            self.skipTest("RawIOBase.readinto not implemented")
        array = array.array("b", b"xyz")
        io.BytesIO(b"abc").readinto(array)
        self.assertEqual(b"abc", array.tobytes())

    def test_readinto_memoryview(self):
        if not READ_SUPPORT:
            self.skipTest("RawIOBase.readinto not implemented")
        mv = memoryview
