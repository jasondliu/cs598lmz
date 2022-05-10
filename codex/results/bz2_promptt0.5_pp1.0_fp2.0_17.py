import bz2
# Test BZ2Decompressor
#
# This tests the decompressor object, which is the most important part of
# the BZ2File implementation.

import bz2
import io
import os
import sys
import tempfile
import unittest
from test import support
from test.support import TESTFN, unlink

# Test data

# Some random data
data = b'BZh91AY&SY\xd0\x00\x00\x00\x80\x00\x10@\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00
