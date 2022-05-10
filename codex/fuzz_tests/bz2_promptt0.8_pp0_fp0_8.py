import bz2
# Test BZ2Decompressor on a short file
# This can be used to test BZ2Decompressor.__init__, __del__, __repr__, and
# decompress methods.

import bz2
import os
import test.support
from test.support import TESTFN, run_unittest
import unittest

data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?\xe7\xff\xe00\x01\x99\xaa\x00\xc0\x03F' + \
       b'\xc0\x85\x00 \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

class BZ2FileTestCase(unittest.TestCase):

    def setUp(self):
        self.filename = TESTFN
        self.contents = data * 10

    def tearDown(self
