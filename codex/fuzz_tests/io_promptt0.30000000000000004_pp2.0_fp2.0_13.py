import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref

from test import support
from test.support import TESTFN, run_unittest, unlink, import_module
from test.support.script_helper import assert_python_ok

# Base for testing file IO

class BaseTestIO(unittest.TestCase):

    def setUp(self):
        self.f = self.FileIO(TESTFN, 'w+')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def testWeakRefs(self):
        # verify weak references
        p = weakref.proxy(self.f)
        self.assertEqual(p.mode, self.f.mode)
        self.assertEqual(p.name, self.f.name)
        self.assertEqual(p.closed, self.f.closed)
        self.assertRaises(TypeError, type, p)
        self.assertRaises(ReferenceError
