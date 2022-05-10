import io
# Test io.RawIOBase

import time
import unittest
from test.support import TESTFN, run_unittest, skip_unless_symlink
from test.support import _2G, _4G, _4Gplus1
from io import BytesIO, BufferedReader, BufferedWriter, BufferedRWPair, \
     BufferedRandom, TextIOWrapper, UnsupportedOperation
from io import DEFAULT_BUFFER_SIZE as BUFSIZE
from io import SEEK_SET, SEEK_CUR, SEEK_END
from io import BufferedReader as RawIO
import os
import sys

class BaseTestCase(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'w+b', 0)
        self.f.write(b'abc\n')
        self.f.write(b'abc\n')
        self.f.flush()
        self.f.seek(0, 0)

    def tearDown(self):
        if self.f:
            self.f.close()
        os.un
