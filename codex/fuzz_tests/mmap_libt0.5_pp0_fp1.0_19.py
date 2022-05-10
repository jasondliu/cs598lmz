import mmap
import os
import re
import sys
import traceback
import types
import unittest
import warnings

# Modules under test
import pydoc
import pydoc_data

from test.support import captured_stdout, captured_stderr, run_unittest, \
    forget, check_warnings, run_with_locale, unload
from test.support.script_helper import assert_python_ok, assert_python_failure

# Stuff to test
from pydoc import *
from pydoc_data import topics as _topics

# Modules used by the tests
import test.pydoc_mod
from test.pydoc_mod import *
import test.support

# Modules that should be documented
import pydoc
import pydoc_data

# Modules that should not be documented
import locale
import time
import sys
import builtins
import __main__

# Stuff to document
class TestClass:
    """This is a test class."""

    def test_method(self):
        """This is a test
