import mmap
import os
import re
import sys
import tempfile
import threading
import time
import traceback
import unittest
import weakref

from test import support
from test.support import os_helper
from test.support.script_helper import assert_python_ok
from test.support.script_helper import assert_python_failure

# Skip these tests if a memmapping implementation is not available.
try:
    import mmap
except ImportError:
    raise unittest.SkipTest("mmap not available")

# Skip these tests if the _testcapi module isn't available.
support.import_module('_testcapi')

from _testcapi import getargs_b, getargs_B, getargs_h, getargs_H
from _testcapi import getargs_i, getargs_I, getargs_k, getargs_K
from _testcapi import getargs_n, getargs_n_impl, getargs_N, getargs_N_impl
from _testcapi import getargs_l, getargs_L,
