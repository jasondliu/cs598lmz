import lzma
lzma.LZMAError

import os
import sys
import time
import shutil
import subprocess
import tempfile
import unittest
import warnings

from test import support
from test.support import TESTFN, run_unittest, unlink, unload
from test.support.script_helper import assert_python_ok

# Skip test if the implementation is CPython and the version is less than 3.3.
requires_lzma = unittest.skipUnless(
    lzma.LZMAFile,
    "requires backported lzma module from PyPI")

requires_lzma_version = unittest.skipUnless(
    lzma.LZMAFile,
    "requires backported lzma module from PyPI")

requires_lzma_version(3, 3)(unittest.skipUnless)(
    sys.version_info >= (3, 3),
    "requires Python 3.3 or later")

requires_lzma_version(3, 4)(unittest.skipUnless)(
    sys.version_info >= (
