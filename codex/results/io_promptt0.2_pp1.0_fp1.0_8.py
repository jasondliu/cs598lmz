import io
# Test io.RawIOBase

import io
import unittest
import weakref
import os
import sys
import errno
import _io
import _testcapi
import pickle
import tempfile
import contextlib
import gc
import shutil

from test import support
from test.support import import_fresh_module

# Base test class for testing IOBase and its subclasses

class BaseTestIO(unittest.TestCase):

    def setUp(self):
        self.f = self.StringIO("\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTU
