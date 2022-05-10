import mmap
import os
import platform
import subprocess
import sys
import textwrap
import timeit
import unicodedata
import warnings
import unittest

from test import support
from test.script_helper import assert_python_ok

# Load the _testcapi module.
import _testcapi

#  _XOPEN_SOURCE >= 600 or _ISOC99_SOURCE: use of %f format for float and %zd
#  for size_t.
requires_IEEE_754 = support.requires_IEEE_754
requires_IEEE_754_format = support.requires_IEEE_754_format
requires_z_format = support.requires_z_format

#  Needed for WSAGetLastError on Windows.
if sys.platform == 'win32':
    import ctypes

# For the check_warnings function
from contextlib import contextmanager

def check_py3k_warnings():
    if sys.py3kwarning:
        return True
    # Python < 2.6 doesn't have this attribute. The absence of the module
    #
