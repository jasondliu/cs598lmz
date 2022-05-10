import lzma
# Test LZMADecompressor.decompress() method
#
# This test is based on
# https://github.com/python/cpython/blob/master/Lib/test/test_lzma.py
#
# Copyright (c) 2004-2020 Python Software Foundation; All Rights Reserved
# Copyright (c) 2001-2020 Python Software Foundation; All Rights Reserved
#
# Author: Victor Stinner

import unittest
import io
import os
import struct
import sys
import tempfile
import warnings
from test import support
from test.support import TESTFN, run_unittest, import_module

try:
    import bz2
except ImportError:
    bz2 = None

try:
    import zlib
except ImportError:
    zlib = None

try:
    import brotli
except ImportError:
    brotli = None

try:
    import lzma
except ImportError:
    lzma = None

try:
    import zstd
except ImportError:
    zstd = None

# Test data generated with:
#
#   import l
