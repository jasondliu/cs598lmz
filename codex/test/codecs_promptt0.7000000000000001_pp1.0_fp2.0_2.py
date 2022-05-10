import codecs
# Test codecs.register_error()
#
# This test modifies the global variables used by codecs.register_error()
# so it should not be run in parallel with other tests.
#
# This test is not run on Windows, as Windows doesn't support the
# os.dup() call that is used to check that the error handler is
# duplicated properly.
import os
import unittest

# Skip this test on Windows. It uses os.dup(), which is not
# available on Windows.
if os.name == 'nt':
    raise unittest.SkipTest("os.dup() is not available on Windows")

import sys

