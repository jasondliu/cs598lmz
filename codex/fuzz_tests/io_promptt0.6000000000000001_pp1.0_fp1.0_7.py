import io
# Test io.RawIOBase
import io
import socket
import tempfile
import unittest
import warnings

import test.support
from test.support import bigaddrspacetest, TESTFN, unlink, run_unittest

# Needed for socket tests.
HOST = 'localhost'

class AutoFileTests(unittest.TestCase):
    # file tests for which a test file is automatically set up

    def setUp(self):
        self.f = open(TESTFN, 'w+')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def testWeakRefs(self):
        # verify weak references
        p = proxy(self.f)
        p.write('test')
        p.seek(0)
        self.assertEqual(p.read(), 'test')
        del self.f
        self.assertEqual(p.read(), 'test')

    def testAttributes(self):
        # verify expected attributes exist
        f = self.f
        f.write('test
