import io
# Test io.RawIOBase methods

import _thread

try:
    import _testinternalcapi
except ImportError:
    _testinternalcapi = None

try:
    from _testcapi import getargs_eintr
except ImportError:
    getargs_eintr = None

import os
import sys
import unittest
import weakref
from test import support
from test.support import TESTFN, unlink, captured_stdout
try:
    import resource
except ImportError:
    resource = None

try:
    import ctypes
except ImportError:
    ctypes = None

# XXX A good test for a readinto() implementation would be
# to produce a mish-mash IO object that reads some bytes with
# read(), some with readinto(), and some with both.  It should
# be readable with file.read() and array.array().

# XXX A good test for a write() implementation would be
# to produce a mish-mash IO object that writes some bytes with
# write(), some with readfrom(), and some with both.  It should
# be writable with file
