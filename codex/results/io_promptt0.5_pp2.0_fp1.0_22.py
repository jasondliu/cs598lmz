import io
# Test io.RawIOBase

# This file contains test cases for the io module.  To run it, do:
#
#     python test_io.py
#
# It requires the pyexpat and select modules, which are standard in
# Python 2.0 and later.

import unittest
from test import support
from test.support import import_module
import os
import sys
import errno
import io
import tempfile
import random
import shutil
import stat
import struct
import subprocess
import warnings
import weakref
import gc
import contextlib
import functools

# Skip these tests if the _io module isn't available.
_io = support.import_module('_io')

# Optionally test the Python implementation
try:
    import _pyio as pyio
except ImportError:
    pyio = None

# Skip these tests if the _testcapi module isn't available.
_testcapi = support.import_module('_testcapi')

# Optionally test the C implementation
try:
    import _cio
except ImportError:
    _cio =
