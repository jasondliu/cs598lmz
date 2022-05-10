import io
# Test io.RawIOBase
import abc

class RawIOBaseTest(unittest.TestCase):

    def test_abc(self):
        self.assertIsInstance(io.RawIOBase, abc.ABCMeta)
        self.assertTrue(issubclass(io.RawIOBase, io.IOBase))

    def test_attributes(self):
        self.assertIsInstance(io.RawIOBase.name, str)
        self.assertIsInstance(io.RawIOBase.mode, str)
        self.assertIsInstance(io.RawIOBase.closed, bool)
        self.assertIsInstance(io.RawIOBase.readable, bool)
        self.assertIsInstance(io.RawIOBase.writable, bool)
        self.assertIsInstance(io.RawIOBase.seekable, bool)

    def test_unsupported_operations(self):
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readline()
        with self.assertRaises(io.UnsupportedOperation):
            io.RawIOBase().readlines()
