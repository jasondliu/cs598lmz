import bz2
# Test BZ2Decompressor (compressor=bz2.BZ2Compressor()).

import copy
import io
import os
import os.path
import pickle
import struct
import tempfile
import unittest
from test import support
from test.support import (TESTFN, run_unittest, check_warnings,
                          check_impl_detail, unlink)
from test import test_support
try:
    import threading
except ImportError:
    threading = None


def write_bz2file(filename, data, compresslevel=9):
    """Write `data` to `filename` using the "bz2" format.

    The compression level `compresslevel` is used.
    """
    with bz2.BZ2File(filename, "wb", compresslevel) as f:
        f.write(data)


def read_bz2file(filename, mode="rb"):
    """Read data from `filename` using the "bz2" format.

    Return the data.
    """
    data = []
    with bz2.BZ2
