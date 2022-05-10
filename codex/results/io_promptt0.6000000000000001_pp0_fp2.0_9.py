import io
# Test io.RawIOBase.
#
# Tested methods:
#   __init__
#   readall
#   readinto
#   read
#   write
#   close
#   fileno
#   isatty
#   seek
#   seekable
#   tell
#   truncate
#   readable
#   writable
#   seekable
#   __repr__
#
# The RawIOBase implementation is used in the implementation of the
# BufferedIOBase and TextIOBase classes.

# Bypass the import machinery for io and _pyio.
# This is necessary because io and _pyio both import each other.
# When running this test, the import machinery has been disabled,
# but we still need the _pyio module for this test.
import sys
import _io
sys.modules['_io'] = _io
sys.modules['io'] = _io


from _pyio import __doc__, RawIOBase
from _pyio import _DEFAULT_BUFFER_SIZE
from _pyio import UnsupportedOperation
import unittest
from test import test_support as support

