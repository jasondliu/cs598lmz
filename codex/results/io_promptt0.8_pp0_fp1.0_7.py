import io
# Test io.RawIOBase class

class RawIOTest(unittest.TestCase):

    def test_class(self):
        self.assertIsInstance(io.RawIOBase, type)
        self.assertEqual(io.RawIOBase.__name__, "RawIOBase")
        self.assertEqual(io.RawIOBase.__doc__,
            "Base class for raw binary I/O.")
        self.assertTrue(io.RawIOBase.close)
        self.assertTrue(io.RawIOBase.closed)
        self.assertTrue(io.RawIOBase.flush)
        self.assertTrue(io.RawIOBase.isatty)
        self.assertTrue(io.RawIOBase.read)
        self.assertTrue(io.RawIOBase.readinto)
        self.assertTrue(io.RawIOBase.readline)
        self.assertTrue(io.RawIOBase.seek)
        self.assertTrue(io.RawIOBase.seekable)
        self.assertTrue(io.RawIOBase.tell)
        self.assertTrue
