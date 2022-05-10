import io
# Test io.RawIOBase classes

import io
import os
import sys
import warnings
import unittest

from test.support import run_unittest, import_module, TESTFN
from test.support.script_helper import assert_python_ok

# Helper to exit the test when we're not running headless
import sys
import os

def _get_display():
    try:
        import ctypes
    except ImportError:
        return None

    try:
        lib = ctypes.cdll.LoadLibrary('libc.so.6')
        lib.getenv.restype = ctypes.c_char_p
        return lib.getenv('DISPLAY')
    except (OSError, AttributeError):
        return None

def _get_display_env():
    return os.environ.get("DISPLAY")


def _have_display():
    return any(filter(None, (_get_display(), _get_display_env())))


if (not hasattr(os, "fork")) or (not _have_display()):
    raise unittest.SkipTest
