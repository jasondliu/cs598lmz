import io
# Test io.RawIOBase.

import io
import os
import sys
import unittest
from io import BytesIO, BufferedReader, BufferedWriter, BufferedRWPair, BufferedRandom
from io import DEFAULT_BUFFER_SIZE
from test import support

# A utility function to make a memory-mapped file.
def make_mmap_file(name, contents):
    with open(name, 'wb') as f:
        f.write(contents)
    return mmap.mmap(f.fileno(), len(contents))

class AutoFileTests(unittest.TestCase):
    # file tests for which a file is automatically set up

    def setUp(self):
        self.f = open(support.TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(support.TESTFN)

    def testWeakRefs(self):
        # verify weak references
        p = proxy(self.f)
        p.write(b"xxx")
       
