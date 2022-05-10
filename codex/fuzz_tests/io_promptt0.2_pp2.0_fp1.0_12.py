import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import errno
import stat
import weakref
from test import support
from test.support import TESTFN, run_unittest, unlink, import_module
from test.support.script_helper import assert_python_ok
from test.support.os_helper import TESTFN_UNICODE

# Base class for testing a RawIO implementation.
# The class to test is given as the 'io' class attribute.
# A few standard tests are skipped, and the standard test_readline()
# is replaced by a simple read().
#
# The setUp() method creates a test file, and the tearDown() method
# deletes it.  To test a different file, override setUp().
# To avoid deleting the file, override tearDown() with a no-operation.
#
# Subclasses should override the standard tests that are skipped.
#
# The test file is created with contents 'test' * 2**16.
# To test a different file, override setUp().

class BaseRawIO(unittest.
