import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import stat
import weakref
import contextlib
import random
import shutil
import warnings
import functools
import gc
import struct
import array
import mmap
import _pyio as pyio

from test import support
from test.support import TESTFN, unlink, unlink, run_with_locale
from test.support.script_helper import assert_python_ok

# Test the raw I/O implementation

TEST_FILENAME = TESTFN

class AutoFileTests(unittest.TestCase):
    # file tests for which a file is automatically set up

    def setUp(self):
        self.f = io.FileIO(TESTFN, 'w+')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def testWeakRefs(self):
        # verify weak references
        p = weakref.proxy(self.f)
        p.
