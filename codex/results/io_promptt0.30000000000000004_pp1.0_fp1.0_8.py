import io
# Test io.RawIOBase

import io
import _io
import unittest
import weakref
import os
import errno
import sys
import subprocess
import tempfile
import stat

from test import support
from test.support import import_helper

# The reference implementation is in Python, not C.
try:
    import _io
except ImportError:
    _io = None

# Skip tests if the _io module isn't available.
requires_Io = unittest.skipUnless(_io, '_io module required')

# Skip tests if the _testcapi module isn't available.
_testcapi = import_helper.import_module('_testcapi')
requires_testcapi = unittest.skipUnless(_testcapi, '_testcapi module required')

# Skip tests if the _multiprocessing module isn't available.
_multiprocessing = import_helper.import_module('_multiprocessing')
requires_multiprocessing = unittest.skipUnless(
    _multiprocessing, '_multipro
