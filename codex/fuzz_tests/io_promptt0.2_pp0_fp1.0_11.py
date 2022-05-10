import io
# Test io.RawIOBase

import _io
import io
import unittest
import weakref
import sys
import os
import errno
import gc
import time
import threading
import subprocess
import select
import socket
import warnings

from test import support
from test.support import TESTFN, run_with_locale, unlink, import_module

# Skip tests if _multiprocessing wasn't built.
mp = import_module('_multiprocessing')
sem = import_module('multiprocessing.synchronize')

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import msvcrt
except ImportError:
    msvcrt = None

try:
    import _winapi
except ImportError:
    _winapi = None

# Some tests need a file with at least 512 bytes.
FILE_SIZE = 512

# Some tests need a non-ascii filename.
TESTFN_UNICODE = TESTFN + "ą"

def _check_warnings(
