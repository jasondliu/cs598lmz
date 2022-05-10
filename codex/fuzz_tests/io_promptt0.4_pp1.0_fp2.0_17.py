import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import struct
import random
import time
import weakref

from test import test_support
from test.test_support import TESTFN, run_with_locale

# Check that the attributes exist
io.IOBase.name
io.IOBase.mode

class AutoFileTests(unittest.TestCase):
    # file tests for which a file is automatically set up

    def setUp(self):
        # Automatically set up a file for reading/writing
        self.file = tempfile.TemporaryFile()
        self.addCleanup(self.file.close)

    def testWeakRefs(self):
        # verify weak references
        p = weakref.proxy(self.file)
        p.write(bytes(range(10)))
        p.seek(0)
        self.assertEqual(self.file.read(), bytes(range(10)))

    def testAttributes(self):
        # verify expected attributes exist
        f = self.file
        f.name
