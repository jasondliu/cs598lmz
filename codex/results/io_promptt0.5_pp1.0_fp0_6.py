import io
# Test io.RawIOBase

import _io
import unittest

class RawIOTest(unittest.TestCase):

    def test_read(self):
        self.assertTrue(issubclass(io.RawIOBase, _io.IOBase))
        self.assertEqual(io.RawIOBase.read.__doc__,
                         'Read at most n bytes, returned as bytes.')
        self.assertEqual(io.RawIOBase.read1.__doc__,
                         'Read up to n bytes with at most one read() system call.')
        self.assertEqual(io.RawIOBase.write.__doc__,
                         'Write the given bytes or bytearray object, returning '
                         'the number of bytes written.')
        self.assertEqual(io.RawIOBase.fileno.__doc__,
                         'Returns underlying file descriptor if one exists.')
        self.assertEqual(io.RawIOBase.readable.__doc__,
                         'True if the IO object can be read.')
        self.assertEqual(io.RawIOBase
