import lzma
lzma.LZMAError

# This is a workaround for a bug in Python 3.5.0.
# See https://bugs.python.org/issue25150
# and https://github.com/python/cpython/commit/e3a1c7f2f8b9c9b9a9a4e4e8f8d1f7b2a4b9f9b1
# for more information.
import sys
if sys.version_info[:3] == (3, 5, 0):
    import _lzma
    _lzma.LZMAError = lzma.LZMAError

import os
import sys
import subprocess
import shutil
import tempfile
import unittest
import warnings

from test import support
from test.support import TESTFN, run_unittest, unlink, import_module

# Skip this test if the implementation doesn't support lzma compression.
lzma = import_module('lzma')

# Skip this test if the implementation doesn't support text mode.
try:
    lz
