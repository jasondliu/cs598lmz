import io
# Test io.RawIOBase

import _io
import unittest
import weakref
import os
import sys
import io
import pickle
import gc
import threading
import subprocess
import errno
import socket
import select
import time
import struct
import tempfile
import shutil

from test import support
from test.support import TESTFN, unlink, run_with_locale
from test.support.script_helper import assert_python_ok

# This is a base class for testing io.IOBase derived classes.
# It defines a few methods that are used by the tests.

# A mixin for testing RawIOBase
class RawIOMixin:
    # A mixin defining tests relating to the RawIOBase interface.

    # This is a base class defining tests common to all RawIOBase
    # implementations.  It doesn't define any tests of its own, but
    # defines a few methods that are used by the tests defined in
    # test_io.

    # A few sample strings for use in testing
    _sample_len = 100
    _sample_data = b'abc\n
