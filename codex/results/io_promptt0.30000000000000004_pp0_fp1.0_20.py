import io
# Test io.RawIOBase
class RawIOTest(unittest.TestCase):
    def test_rawio(self):
        self.assertTrue(issubclass(io.RawIOBase, io.IOBase))
        self.assertTrue(issubclass(io.FileIO, io.RawIOBase))
        self.assertTrue(issubclass(io.BufferedIOBase, io.IOBase))
        self.assertTrue(issubclass(io.BufferedReader, io.BufferedIOBase))
        self.assertTrue(issubclass(io.BufferedWriter, io.BufferedIOBase))
        self.assertTrue(issubclass(io.BufferedRWPair, io.BufferedIOBase))
        self.assertTrue(issubclass(io.TextIOBase, io.IOBase))
        self.assertTrue(issubclass(io.TextIOWrapper, io.TextIOBase))
        self.assertTrue(issubclass(io.StringIO, io.TextIOBase))
        self.assertTrue(issubclass(io.BytesIO, io.BufferedIO
