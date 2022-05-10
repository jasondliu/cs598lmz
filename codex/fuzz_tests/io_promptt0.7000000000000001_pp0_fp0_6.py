import io
# Test io.RawIOBase
from io import RawIOBase
from io import _IOBase
# Test io.BufferedIOBase
from io import BufferedIOBase
from io import _BufferedIOBase
# Test io.TextIOBase
from io import TextIOBase
from io import _TextIOBase
# Test io.FileIO
from io import FileIO
from io import _FileIO
# Test io.BytesIO
from io import BytesIO
from io import _BytesIO


class TestCase(unittest.TestCase):

    def test_RawIOBase(self):
        self.assertTrue(issubclass(RawIOBase, _IOBase))

    def test_BufferedIOBase(self):
        self.assertTrue(issubclass(_IOBase, BufferedIOBase))
        self.assertTrue(issubclass(BufferedIOBase, _BufferedIOBase))

    def test_TextIOBase(self):
        self.assertTrue(issubclass(_IOBase, TextIOBase))
        self.assertTrue(issubclass(_BufferedIOBase, TextIOBase))
        self.assertTrue
