import lzma
# Test LZMADecompressor

# Test the LZMADecompressor class.

# This is a very simple test, it only tests that the decompressor
# accepts the same input as the reference implementation.

# The test files are created by compressing the files in the
# CPython Lib/test/input directory with the command
# xz -z -c -9 < file > file.xz

# The test files were created with xz 5.1.2alpha from
# http://tukaani.org/xz/xz-5.1.2alpha.tar.gz

# The reference decompressor is available at
# http://tukaani.org/xz/xz-5.1.2alpha.tar.gz

import os
import struct
import subprocess
import sys
import unittest
import warnings
import zlib

import test.support

from test.support import TESTFN, run_unittest, import_module, unlink

try:
    import _lzma
except ImportError:
    _lzma = None

TEST_FILES = [
   
