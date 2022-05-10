import io
# Test io.RawIOBase

import unittest
import io
import os
import sys
import tempfile
import weakref
import warnings
from test import support
from test.support import TESTFN, unlink, run_unittest, import_module
from test.support.script_helper import assert_python_ok

# Base class for testing a RawIO implementation.
# The class to test is given as the 'io' class attribute.
#
# To test an implementation, derive a class which overrides setUp(),
# tearDown(), and any other applicable methods.  The derived instance
# should be passed to the test_main() function.
#
# Alternatively, the derived class can override the 'io' class attribute
# with an instance of the implementation to test.
#
# The setUp() method can assume that the 'io' attribute is a RawIOBase
# subclass.  It should create an instance and assign it to the 'r'
# attribute.  The tearDown() method should close the 'r' attribute, if
# it exists.
#
# The test methods should use the 'r' attribute for all IO operations.
#
