import io
# Test io.RawIOBase

import _io
import io
import os
import sys
import unittest
from test import support
from test.support import TESTFN, unlink

# Issue #11459: check that io.open() accepts a unicode filename.
support.check_impl_detail(
    io, 'open',
    lambda name, mode='r', buffering=-1, encoding=None, errors=None,
    newline=None, closefd=True, opener=None:
        isinstance(name, str))

# Issue #11459: check that io.FileIO() accepts a unicode filename.
support.check_impl_detail(
    io, 'FileIO',
    lambda name, mode='r', closefd=True, opener=None:
        isinstance(name, str))

# Issue #11459: check that io.BytesIO() accepts a unicode filename.
support.check_impl_detail(
    io, 'BytesIO',
    lambda initial_bytes=None, newline=None:
        isinstance(initial_bytes, bytes))

# Issue #11459: check
