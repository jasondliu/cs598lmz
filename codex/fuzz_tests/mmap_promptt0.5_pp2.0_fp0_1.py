import mmap
# Test mmap.mmap()
#
# This is a test of the mmap.mmap() function.
#
# See:
# http://docs.python.org/2/library/mmap.html

from errno import *

from test import support
import unittest
import mmap
import os
from mmap import _mmap_close
from mmap import _mmap_find_unused_handle
from mmap import _mmap_find_unused_handle_posix
from mmap import _mmap_find_unused_handle_windows
import sys
import subprocess
import tempfile
import time
import contextlib
import struct
import io
from test.support import TESTFN, run_unittest, import_module, cpython_only
from test.support.script_helper import assert_python_ok
from test.support.os_helper import TESTFN_UNENCODABLE
import random

if not hasattr(mmap, 'ACCESS_READ'):
    raise unittest.SkipTest("mmap module has no attribute ACCESS_READ")

# Test whether
