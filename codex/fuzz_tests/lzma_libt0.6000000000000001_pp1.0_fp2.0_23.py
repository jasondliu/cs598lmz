import lzma
lzma.LZMAError

module_name = "lzma"

from lzma import *

import unittest
from test.support import run_unittest, import_module


class LZMAFileTestCase(unittest.TestCase):

    def setUp(self):
        self.data = b"a" * 10000
        self.xzpath = import_module('test.test_lzma').__file__.rstrip('co')
        self.xzpath += "xz"
        self.lzpath = import_module('test.test_lzma').__file__.rstrip('co')
        self.lzpath += "lz"

    def test_read(self):
        with open(self.xzpath, 'rb') as f:
            self.assertEqual(lzma.decompress(f.read()), self.data)
        with open(self.lzpath, 'rb') as f:
            self.assertEqual(lzma.decompress(f.read()), self
