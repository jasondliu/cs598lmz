import io
# Test io.RawIOBase

import io
import unittest
import weakref
import os
import sys
import threading
import time
import errno
import select
import socket
import subprocess
import tempfile
import shutil

from test import test_support
from test.test_support import TESTFN, run_with_locale, check_warnings

# Use a small buffer size to exercise buffering code.
BUFSIZE = 5

class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.f = io.open(TESTFN, 'w', buffering=0)

    def tearDown(self):
        if self.f:
            self.f.close()
        os.unlink(TESTFN)

    def testWeakRefs(self):
        # verify weak references
        p = weakref.proxy(self.f)
        self.assertEqual(p.mode, self.f.mode)
        self.assertEqual(p.name, self.f.name)
        self.assertEqual(p.close(), None
