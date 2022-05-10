import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import stat
import time
import random
import warnings
import weakref
from test import support
from test.support import TESTFN, unlink, run_unittest, import_module
from test.support.script_helper import assert_python_ok

# Base class for testing a given RawIO implementation.
# Subclasses must override read(), seek(), and write().
class BaseRawIOTest:
    def setUp(self):
        # Base class creates self.rawio
        self.data = b"ABCDE"
        self.len = len(self.data)
        self.rawio.write(self.data)
        self.rawio.seek(0)

    def read(self, n=-1):
        return self.rawio.read(n)

    def seek(self, pos, whence=0):
        return self.rawio.seek(pos, whence)

    def write(self, b):
        return self.rawio.write(b)

    def test
