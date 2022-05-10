import io
# Test io.RawIOBase

import _pyio as pyio
import _testcapi
import abc
import codecs
import errno
import os
import pickle
import random
import re
import select
import struct
import sys
import tempfile
import threading
import time
import unittest
import warnings
from test import support
try:
    import resource
except ImportError:
    resource = None
import faulthandler

try:
    import nt
except ImportError:
    nt = None

# This is used here and in test_bufferedio and test_fileio.
import io

try:
    from io import BlockingIOError
except ImportError:
    BlockingIOError = None

# Disable tests using 'self.assertRaisesRegex'
# because it was added in Python 3.7
TEST_RAISES_REGEX = hasattr(unittest.TestCase, 'assertRaisesRegex')

# --------------------------------------------------------------------
# Generic support

class ExceptionTests(unittest.TestCase):

    def test_io_exceptions(self):
