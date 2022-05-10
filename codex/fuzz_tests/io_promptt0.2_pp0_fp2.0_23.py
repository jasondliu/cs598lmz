import io
# Test io.RawIOBase

import _io
import unittest
import weakref

from test import support
from test.support import import_fresh_module

# Base for testing io.RawIOBase

class BaseTestRawIO(object):

    # Subclass must define the following attributes:
    # - self.filename
    # - self.mode
    # - self.b_prefix
    # - self.has_unseekable_works
    # - self.has_tell_works
    # - self.has_seek_works
    # - self.has_truncate_works
    # - self.readable
    # - self.writable
    # - self.seekable
    # - self.readable_w
    # - self.writable_w
    # - self.seekable_w
    # - self.seek_tell_works
    # - self.seek_whence_1_works
    # - self.seek_whence_2_works
    # - self.seek_whence_3_works
    # - self.seek_whence_4_works
   
