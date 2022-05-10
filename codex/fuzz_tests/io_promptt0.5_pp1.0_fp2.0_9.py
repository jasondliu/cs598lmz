import io
# Test io.RawIOBase
try:
    io.RawIOBase.read
except AttributeError:
    import unittest
    raise unittest.SkipTest("test_io requires io.RawIOBase.read()")

import os
import sys
import unittest

from test import support
from test.support import TESTFN, import_module, unlink

# Skip this test if the _pyio module isn't available.
_pyio = import_module('_pyio')

# Skip this test if the _testcapi module isn't available.
_testcapi = import_module('_testcapi')


class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.f = io.open(TESTFN, "w+", encoding="utf-8")

    def tearDown(self):
        if not self.f.closed:
            self.f.close()
        unlink(TESTFN)

    def testWeakRefs(self):
        # Verify weak references
        p = proxy(self.f)
        p.write("
