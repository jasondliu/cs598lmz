import lzma
# Test LZMADecompressor.read1()

# This test is based on test_lzma.py.

import array
import io
import os
import struct
import sys
import tempfile
import unittest
import warnings
from test import support
from test.support import bigmemtest, import_helper
from test.support.script_helper import assert_python_ok

# Skip test if the implementation is known to be broken.
requires_working_lzma = unittest.skipUnless(
    import_helper.import_module('lzma').LZMADecompressor,
    'requires a working lzma module')
requires_lzma_version = unittest.skipUnless(
    hasattr(lzma, 'LZMA_VERSION'),
    'requires lzma.LZMA_VERSION')
requires_lzma_format = unittest.skipUnless(
    hasattr(lzma, 'FORMAT_XZ'),
    'requires lzma.FORMAT_XZ')
requires_lzma_check = unittest.skipUnless(

