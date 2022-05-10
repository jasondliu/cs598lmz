import gc, weakref
import sys
import time
import traceback

from . import _testcapi
from . import py3kwarn
from . import unittest
from .support import gc_collect, gc_collect_harder, is_jython, is_cli, is_android, is_cpython

# Skip these tests if the _testcapi module isn't available.
requires__testcapi = unittest.skipUnless(
        hasattr(_testcapi, 'with_tp_del'),
        'requires _testcapi')

# Skip these tests if the _testcapi module isn't available.
requires_unicode = unittest.skipUnless(
        hasattr(_testcapi, 'with_tp_del_unicode'),
        'requires _testcapi.with_tp_del_unicode')

# Skip these tests if the _testcapi module isn't available.
requires_unicode_with_docstring = unittest.skipUnless(
        hasattr(_testcapi, 'with_tp_del_unicode_with_docstring'),
        'requires
