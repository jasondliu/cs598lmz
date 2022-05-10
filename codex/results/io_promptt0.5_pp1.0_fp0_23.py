import io
# Test io.RawIOBase

import _pyio as pyio
import _testcapi
import abc
import errno
import os
import random
import select
import signal
import subprocess
import sys
import threading
import time
import unittest

from test import support
from test.support import (
    TESTFN, run_with_locale, check_warnings, bigmemtest, bigaddrspacetest,
    forget)

try:
    import thread
except ImportError:
    thread = None


class AutoFileTests(unittest.TestCase):

    def setUp(self):
        self.f = io.open(TESTFN, 'wb', buffering=0)

    def tearDown(self):
        if self.f is not None:
            self.f.close()
        support.unlink(TESTFN)

    def test_invalid_mode(self):
        with self.assertRaises(ValueError):
            io.open(TESTFN, 'b')
        with self.assertRaises(ValueError):
            io.open(TEST
