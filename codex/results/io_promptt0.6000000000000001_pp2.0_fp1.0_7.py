import io
# Test io.RawIOBase

import unittest
import io
import os
import errno
import sys
import pickle
import shutil
import tempfile
import abc
import stat

try:
    import threading
except ImportError:
    threading = None

import test.support
from test.support import import_module, run_unittest, TESTFN, unlink

# Test running as a script
import os
script_with_universal_newlines = os.path.join(os.path.dirname(__file__),
                                              "io_universal_newlines.py")


class AutoFileTests(unittest.TestCase):
    # file tests for which a test file is automatically set up

    def setUp(self):
        self.f = open(TESTFN, 'w+b')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def testWeakRefs(self):
        # verify weak references
        p = proxy(self.f)
        p.write(
