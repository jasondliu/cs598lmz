import io
# Test io.RawIOBase
#
# This test checks that io.RawIOBase works as expected.
#
# Written by Antoine Pitrou <solipsis@pitrou.net>
# Ported to Python 3 by Petr Viktorin <encukou@gmail.com>

import io
import os
import sys
import unittest
import pickle
import struct
import tempfile
import weakref
import random
import contextlib

from test import support
from test.support import TESTFN, unlink, run_unittest

try:
    import threading
except ImportError:
    threading = None

try:
    import _testcapi
except ImportError:
    _testcapi = None

# This is needed to trigger the readinto bug on PyPy.
# The bug is fixed in PyPy 2.0.
PYPY_VERSION = getattr(sys, 'pypy_version_info', None)

# Test RawIOBase using a StringIO object

class TestRawIO(unittest.TestCase):

    def setUp(self):
        self.r = io.
