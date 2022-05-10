import mmap
# Test mmap.mmap with the Python standard library's shelve.
# This of course depends on the CPython implementation details for shelve.
# This is not a very practical module for writing,
# but it is expected to be good for read-only use.

import _testbuffer
from test import test_support
import tempfile
import os
import shutil
import shelve


test_support.run_unittest(
    None, # TODO - add DbfilenameShelf tests when directories are supported
    __name__
)
