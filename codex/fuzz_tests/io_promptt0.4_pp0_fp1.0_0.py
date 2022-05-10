import io
# Test io.RawIOBase

import io
import os
from test import support
import unittest

from test.support import _2G, _4G, _4Gplus1, _test_largefile
from test.support.script_helper import assert_python_ok

# Skip these tests if the platform has no working large file support.
requires_64bit_support = unittest.skipUnless(
        _test_largefile.supports_largefile,
        'test needs 64-bit file support')

# Skip these tests if the platform has no working seek() method.
requires_seek = unittest.skipUnless(
        hasattr(io.RawIOBase, 'seek'),
        'test needs seek() method')

# Skip these tests if the platform has no working tell() method.
requires_tell = unittest.skipUnless(
        hasattr(io.RawIOBase, 'tell'),
        'test needs tell() method')

# Skip these tests if the platform has no working truncate() method.
requires_truncate = unittest.skipUnless(
        hasattr(io.
