import lzma
lzma.LZMA_AVAILABLE = False
lzma.LZMA_PATH = None

import tempfile
import os
import io
import sys
import shutil
import tarfile
import unittest
from test import support
from contextlib import closing
from tarfile import taropen, TarError, TarInfo, ReadError
from tarfile import CompressionError, StreamError

TEMPDIR = tempfile.gettempdir()
prefix = os.path.join(TEMPDIR, "tarfile-testing-")

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.tmpdir = tempfile.mkdtemp(prefix=prefix)
        self.path = os.path.join(self.tmpdir, "tmp")
        self.tar = None

    def tearDown(self):
        if self.tar:
            self.tar.close()
        support.rmtree(self.tmpdir)

    def mktar(self, mode="w", **kwargs):
        self.tar = taropen(self.path,
