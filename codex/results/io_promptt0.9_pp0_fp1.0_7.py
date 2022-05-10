import io
# Test io.RawIOBase interface and interface of input/output streams.

import errno
import functools
import io
import signal
import os
import socket
import sys
import unittest
import _pyio
import gc
import shutil
import tempfile
import textwrap
import warnings
import signal

import test.support
from test.support import import_module, temp_dir, TESTFN, check_warnings

try:
    import threading
except ImportError:
    threading = None

msg123 = b'1\x02hello world\n'
msg1234 = msg123 + b'ab'
msg123n = msg123[:-1]

TEST_DIR = tempfile.gettempdir()
# TESTFN is set in conftest.py
TESTFN2 = TESTFN + "2"

HASH_ROUNDS = 1 # Use more rounds for a real test.

if sys.platform.startswith("win"):
    # Select a non-existent file for Windows error testing.  Windows error
    # messages seem to be localized, and so vary across platforms.
