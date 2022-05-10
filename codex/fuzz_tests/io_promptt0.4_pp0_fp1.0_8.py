import io
# Test io.RawIOBase

import _io

class TestRawIOBase(unittest.TestCase):

    def test_read(self):
        # Test that calling read() without implementing it raises
        # a TypeError.
        with self.assertRaises(TypeError):
            io.RawIOBase().read()

    def test_readinto(self):
        # Test that calling readinto() without implementing it raises
        # a TypeError.
        with self.assertRaises(TypeError):
            io.RawIOBase().readinto(bytearray(10))

    def test_readall(self):
        # Test that calling readall() without implementing it raises
        # a TypeError.
        with self.assertRaises(TypeError):
            io.RawIOBase().readall()

    def test_readinto_unsupported(self):
        # Test that calling readinto() without implementing it raises
        # a TypeError.
        with self.assertRaises(TypeError):
            io.RawIOBase().readinto(bytearray(10))

    def test_readinto_array
