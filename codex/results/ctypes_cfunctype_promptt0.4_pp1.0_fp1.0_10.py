import ctypes
# Test ctypes.CFUNCTYPE

# This test is designed to test the CFUNCTYPE type.  It is not
# designed to test the ctypes module, although it does test some
# features of ctypes.

# This test is designed to be run by the Python regression test
# framework, using the REGRTEST_RUNLINE configuration variable in
# the Modules/Setup file.  It is also designed to be run manually,
# using the '-uall' option.

# The test is designed to be run in a subprocess, so it can't
# directly call unittest.main().  Instead, it uses the regrtest
# support for running a test in a subprocess.

# The test uses the regrtest support for skipping tests.  It is
# skipped if the _ctypes module isn't available.

import sys
import unittest
import _ctypes_test

from ctypes import *

# Check that the _ctypes module is available
try:
    import _ctypes
except ImportError:
    raise unittest.SkipTest("ctypes not available")

# Check that
