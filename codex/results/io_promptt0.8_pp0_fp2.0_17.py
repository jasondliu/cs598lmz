import io
# Test io.RawIOBase with in-memory buffers.

import array
import os
import shutil
import signal
import socket
import sys
import time
import warnings
from test.support import (TESTFN, run_with_locale, check_warnings,
                          strip_python_stderr, check_syntax_error)
import unittest
from unittest import mock
import random

# For controlling the MMAP constant
import mmap as _mmap
mmap = _mmap.mmap
try:
    mmap.DONTNEED
except AttributeError:
    mmap = None

try:
    import threading
except ImportError:
    threading = None

try:
    import _winapi
except ImportError:
    _winapi = None

# We test unicode filenames in the same way as non-unicode ones
# so use str type not bytes for TESTFN
TESTFN = TESTFN.encode('ascii', 'surrogateescape').decode('ascii')

# Filename used for testing
if sys.platform in ("
