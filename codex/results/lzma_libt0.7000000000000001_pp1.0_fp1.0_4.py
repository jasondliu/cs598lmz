import lzma
lzma.LZMADecompressor.flush = lambda self, x: bytes()

class Tests(unittest.TestCase):

    def setUp(self):
        self.data = b'The quick brown fox jumps over the lazy dog'
        self.rs = lzma.LZMARandomStream(self.data, lzma.LZMA_TELL_ANY_CHECK)
        self.rs.seek(0, 2)
        self.size = self.rs.tell()
        self.rs.seek(0)

    def test_tell(self):
        self.assertEqual(self.rs.tell(), 0)
        self.rs.read(1)
        self.assertEqual(self.rs.tell(), 1)
        self.rs.read(2)
        self.assertEqual(self.rs.tell(), 3)
        self.rs.seek(0, 2)
        self.assertEqual(self.rs.tell(), self.size)

    def test_read(self):
        self.assertEqual(self.rs.read
