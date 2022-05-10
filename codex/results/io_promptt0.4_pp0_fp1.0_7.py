import io
# Test io.RawIOBase

import unittest
import os
import io
import sys
import tempfile
import errno
import struct
import random
import stat
import _pyio as pyio
from test import support
from test.support import TESTFN, unlink, run_unittest, import_module
from test.support.script_helper import assert_python_ok

# Windows requires opened files to have the 'read' access right
READ_ACCESS = os.O_RDONLY
if sys.platform == 'win32':
    READ_ACCESS |= os.O_BINARY

class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.f = open(TESTFN, 'wb')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def testWeakRefs(self):
        # verify weak references
        p = pyio.TextIOWrapper(self.f, encoding='ascii')
        p.write('hi')
        q
