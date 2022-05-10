import io
# Test io.RawIOBase methods

# The tests are structured as follows:
#
#   * Each test method tests a specific RawIOBase method
#   * The first part of each method is common to all tests and checks that
#     the test can run with the current implementation of the io module
#   * The second part of each method is specific to the tested method
#

import io
import os
import stat
import struct
import sys
import tempfile
import unittest
import warnings

from test import support

try:
    import fcntl
except ImportError:
    fcntl = None

try:
    import termios
except ImportError:
    termios = None


@unittest.skipUnless(hasattr(os, 'O_RDONLY'), 'requires os.O_RDONLY')
@unittest.skipUnless(hasattr(os, 'O_BINARY'), 'requires os.O_BINARY')
class TestRawIOBase(unittest.TestCase):
    """Tests for RawIOBase implementations.

    The tests are structured as follows:

   
