import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import errno
import functools
import select
import socket
import threading
import time
import warnings
from test import support
from test.support import import_module
from test.support.script_helper import assert_python_ok
from test.support.os_helper import TESTFN, unlink

# Skip tests if there is no os.sendfile()
sendfile = import_module('os').sendfile

# Skip tests if there is no os.sendfile()
sendfile = import_module('os').sendfile

class AutoFileTests(unittest.TestCase):
    def setUp(self):
        self.f = io.FileIO(TESTFN, 'w+')

    def tearDown(self):
        if self.f:
            self.f.close()
        unlink(TESTFN)

    def testWeakRefs(self):
        p = weakref.proxy(self.f)
        f = self.f
        self.f
