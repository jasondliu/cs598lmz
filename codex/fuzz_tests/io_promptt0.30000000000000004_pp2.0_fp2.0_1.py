import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, run_unittest

# Set up some constants
try:
    SEEK_SET = os.SEEK_SET
except AttributeError:
    SEEK_SET = 0
try:
    SEEK_CUR = os.SEEK_CUR
except AttributeError:
    SEEK_CUR = 1
try:
    SEEK_END = os.SEEK_END
except AttributeError:
    SEEK_END = 2

# A couple of utility functions

def check_posix_error(testcase, err, fn, *args):
    try:
        fn(*args)
    except OSError as e:
        testcase.assertEqual(e.errno, err)
    else:
        testcase.fail('Expected OSError: %s not raised' % err)

def check_seek_tell(testcase, f, offset, whence, expected_tell):
    testcase.
