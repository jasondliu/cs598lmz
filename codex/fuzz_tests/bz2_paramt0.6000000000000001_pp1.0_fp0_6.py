from bz2 import BZ2Decompressor
BZ2Decompressor.decompress = _patched_decompress

from io import BytesIO
from os import SEEK_SET
from unittest import TestCase

from bz2file import BZ2File
from bz2file import open as bz2open

from . import data
from . import utils


class TestBZ2File(utils.TempFileMixin, TestCase):

    def test_context_manager(self):
        with bz2open(self.filename, 'wt') as f:
            f.write('foo')
        with bz2open(self.filename, 'rb') as f:
            self.assertEqual(f.read(), b'foo')

    def test_tell(self):
        with bz2open(self.filename, 'wt') as f:
            f.write('foo')
        with bz2open(self.filename, 'rb') as f:
            self.assertEqual(f.tell(), 0)
            f.read(1)
            self.assertEqual(f.tell(), 1)
            f.
