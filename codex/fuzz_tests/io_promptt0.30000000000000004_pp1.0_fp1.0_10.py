import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import errno
import select
import struct
import tempfile
import threading
import subprocess
import time
import warnings
from test import support
from test.support import TESTFN, run_with_locale
from test.support.script_helper import assert_python_ok, assert_python_failure
from test.support.os_helper import TESTFN_UNENCODABLE

# The following tests are not exhaustive.  They are here to catch
# problems early when porting to a new platform.
# More extensive tests are in test_fileio.py and test_bufferedio.py.

# The non-blocking tests are only relevant on systems that support
# os.O_NONBLOCK.
HAVE_NONBLOCK = hasattr(os, 'O_NONBLOCK')

# The test_truncate tests are only relevant on systems that support
# ftruncate().
HAVE_FTRUNCATE = hasattr(os, 'ftruncate')
