import mmap
import os
import re
import subprocess
import sys
import tempfile
import time
import traceback
import unittest

from test import support
from test.support import (
    bigmemtest, bigaddrspacetest, cpython_only,
    captured_stdout, captured_stderr, gc_collect,
    import_module, run_unittest, unlink, unload,
    TESTFN, TESTFN_UNENCODABLE, HOST,
    )
from test.support.script_helper import assert_python_ok

# Skip these tests if a memmory limit is required and the required
# amount of memory is not available.
requires_32b = unittest.skipUnless(
        sys.maxsize <= 2**32,
        "test requires a 32-bit system")
requires_64b = unittest.skipUnless(
        sys.maxsize > 2**32,
        "test requires a 64-bit system")

# Skip these tests if the OS requires a memory limit and the required
# amount of memory is not available.
requires_32
