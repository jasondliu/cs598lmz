import io
# Test io.RawIOBase reading and writing.

class TestRawIOBase(unittest.TestCase):
    def setUp(self):
        self.rawio = io.RawIOBase()

    def test_attributes(self):
        # Attributes are -1, None, or the empty string.
        self.assertEqual(self.rawio.writable(), False)
        self.assertEqual(self.rawio.readable(), False)
        self.assertEqual(self.rawio.seekable(), False)
        self.assertEqual(self.rawio.fileno(), -1)
        self.assertEqual(self.rawio.isatty(), False)
        self.assertEqual(self.rawio.name, '')

        self.assertRaises(OSError, self.rawio.flush)
        self.assertRaises(OSError, self.rawio.tell)

        self.assertRaises(OSError, self.rawio.read, 5)
        self.assertRaises(OSError, self.rawio.write, b"12345")

        #
