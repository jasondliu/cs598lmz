import io
# Test io.RawIOBase

import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest, import_module
from test.support.script_helper import assert_python_ok

# Issue #11395: the C implementation doesn't support tell() or truncate()
requires_IOCAPABILITIES = unittest.skipUnless(
        hasattr(io, 'RawIOBase') and hasattr(io.RawIOBase, 'seekable'),
        'test needs RawIOBase.seekable()')

# Issue #17672: the C implementation doesn't support readinto()
requires_readinto = unittest.skipUnless(
        hasattr(io, 'RawIOBase') and hasattr(io.RawIOBase, 'readinto'),
        'test needs RawIOBase.readinto()')

# Issue #17672: the C implementation doesn't support readinto()
requires_readinto_bytes = unittest.skipUnless(
        hasattr(io, 'RawIOBase') and hasattr(io.RawIOBase, 'readinto
