import codecs
# Test codecs.register_error before importing other modules
# that might also try to register errors.
try:
    codecs.register_error('test.test_codecs', codecs.lookup_error('strict'))
except ValueError:
    pass
import re
import os
import sys
import unittest
import warnings
from test import test_support
from test.test_support import TESTFN, run_unittest, findfile, import_module
from test.script_helper import assert_python_ok
from test import string_tests
from test import test_genericpath
from test import test_support
from test.test_support import TESTFN, run_unittest, import_module
import StringIO
import tempfile
from textwrap import dedent
import unicodedata
from unicodedata import normalize, category
try:
    import cStringIO as StringIO
except ImportError:
    pass

# TESTFN is defined in test.test_support
# TESTFN_UNICODE is defined in test.test_support
# TESTFN_ENCODING is defined in test.test_support

#
