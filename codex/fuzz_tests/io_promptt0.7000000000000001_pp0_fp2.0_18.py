import io
# Test io.RawIOBase

class RawIOBaseTest(unittest.TestCase):
    def test_misc(self):
        self.assertRaises(NotImplementedError, io.RawIOBase().read)
        self.assertRaises(NotImplementedError, io.RawIOBase().readinto)
        self.assertRaises(NotImplementedError, io.RawIOBase().write, b"")
        self.assertRaises(NotImplementedError, io.RawIOBase().seek, 0)
        self.assertRaises(NotImplementedError, io.RawIOBase().tell)
        self.assertRaises(NotImplementedError, io.RawIOBase().truncate)
        self.assertRaises(NotImplementedError, io.RawIOBase().close)
        self.assertTrue(io.RawIOBase().readable())
        self.assertTrue(io.RawIOBase().writable())
        self.assertTrue(io.RawIOBase().seekable())
        self.assertRaises(NotImplementedError, io.RawIOBase().fileno
