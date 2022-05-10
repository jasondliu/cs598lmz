import io
# Test io.RawIOBase

import unittest
from test import support
import os
import sys
import io
import errno
import tempfile
import weakref

class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.f = io.FileIO(__file__, 'r')

    def tearDown(self):
        if self.f:
            self.f.close()

    def testWeakRefs(self):
        p = weakref.proxy(self.f)
        self.assertEqual(p.mode, self.f.mode)
        self.assertEqual(p.name, self.f.name)
        self.f.close()
        self.f = None
        self.assertRaises(ReferenceError, getattr, p, 'mode')

    def testAttributes(self):
        self.assertEqual(self.f.mode, 'r')
        self.assertTrue(self.f.name.endswith('io_tests.py'))
        self.assertTrue(self.f.closed)

    def test
