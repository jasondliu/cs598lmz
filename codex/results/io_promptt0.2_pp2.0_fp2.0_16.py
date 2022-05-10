import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import stat
import time
import struct
import random
import warnings

from test import support
from test.support import TESTFN, run_unittest, import_module, unlink

# Skip tests if there is no implementation of io.RawIOBase
try:
    import _io
except ImportError:
    raise unittest.SkipTest("_io module not available")

# Skip tests if io.RawIOBase is not a type object
if type(_io.RawIOBase) is not type:
    raise unittest.SkipTest("io.RawIOBase is not a type object")

# Skip tests if io.RawIOBase is not a subclass of io.IOBase
if not issubclass(_io.RawIOBase, io.IOBase):
    raise unittest.SkipTest("io.RawIOBase is not a subclass of io.IOBase")

# Skip tests if io.RawIOBase is a direct subclass of io.IOBase
if _io.RawIOBase is io.
