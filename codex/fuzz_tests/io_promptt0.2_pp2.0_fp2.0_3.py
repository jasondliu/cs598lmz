import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support

# Base class for testing RawIOBase
class BaseTestRawIO(object):
    # Subclass must define the following attributes:
    # - self.filename
    # - self.mode
    # - self.b_prefix
    # - self.u_prefix
    # - self.b_suffix
    # - self.u_suffix
    # - self.b_mode
    # - self.u_mode
    # - self.b_encoding
    # - self.u_encoding
    # - self.b_newline
    # - self.u_newline
    # - self.b_errors
    # - self.u_errors
    # - self.b_line_buffering
    # - self.u_line_buffering
    # - self.b_write_through
    # - self.u_write_through
    # - self.b_seekable
    # - self.u_seekable
    # - self.b_readable
   
