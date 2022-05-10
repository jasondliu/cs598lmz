import io
# Test io.RawIOBase

import io
import unittest
import weakref
import os
import sys
import errno
import _pyio as pyio

from test import support
from test.support import TESTFN, run_unittest

class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.f = io.FileIO(TESTFN, 'w+')
        self.f.write(b'abcdefghijklmnop')
        self.f.seek(0, 0)

    def tearDown(self):
        if self.f:
            self.f.close()
        support.unlink(TESTFN)

    def testWeakRefs(self):
        p = weakref.proxy(self.f)
        self.assertEqual(p.tell(), 0)
        self.assertEqual(p.read(1), b'a')
        p.seek(5)
        self.assertEqual(p.read(1), b'f')
        p.close()
        self.assertRaises(ReferenceError,
