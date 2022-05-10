import io
# Test io.RawIOBase for TextIOWrapper's constructor, as happens on
# Python 3.2 on Mac OS X with fast filesystems.

class BrokenRawIO(io.RawIOBase):
    def readable(self):
        return True

    def seekable(self):
        return False

    def readinto(self, b):
        return 0

class TestBrokenSeek(unittest.TestCase):
    def test_constructor(self):
        binary_reader = io.BufferedRandom(BrokenRawIO())
        with self.assertRaises(io.UnsupportedOperation) as cm:
            io.TextIOWrapper(binary_reader)
        self.assertEqual(str(cm.exception),
                         "line buffering requires a buffer that is seekable")

    def test_reopen(self):
        binary_reader = io.BufferedRandom(BrokenRawIO())
        text_reader = io.TextIOWrapper(binary_reader)
        text_reader.close()
        with self.assertRaises(io.UnsupportedOperation) as cm:
            text
