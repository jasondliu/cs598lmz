import lzma
lzma.LZMA_OK
import os
import shutil
import sys
import tempfile
import unittest
from unittest import mock
import warnings
from test import support
from test.support import TESTFN, unlink, run_unittest, import_module
from test.support.script_helper import assert_python_ok, assert_python_failure
from test import script_helper
import unittest.mock
LZMA_SO = os.path.join(os.path.dirname(__file__), 'lzma')
if sys.platform == 'win32':
    LZMA_SO += '.pyd'
else:
    LZMA_SO += '.so'

@unittest.skipUnless(os.path.exists(LZMA_SO), 'requires lzma.so')
class LzmaTestCase(unittest.TestCase):

    def _test_filter_module(self, module_name):
        """Test that the module `module_name` can be loaded and can process
        data."""
        module =
