import mmap
# Test mmap.mmap()
#
# This test is based on the mmap module test, but it is
# simplified to only test the mmap.mmap() function.
#
# The mmap module test is based on the mmapfile test from the
# standard library test suite.

import unittest
import sys
import os
import mmap
import tempfile
import struct
import array
import io
import contextlib
import warnings
import errno

from test import support
from test.support import TESTFN, unlink, unload, run_unittest, import_module
from test.support.script_helper import assert_python_ok

# Skip this test if the _testcapi module isn't available.
_testcapi = import_module('_testcapi')

# Skip this test if the _mmap module isn't available.
_mmap = import_module('_mmap')

# Skip this test if the _multiprocessing module isn't available.
_multiprocessing = import_module('_multiprocessing')

# Skip this test if the _pos
