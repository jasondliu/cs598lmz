import mmap
import os
import re
import shutil
import sys
import tempfile
import time
import unittest
from io import StringIO

from test import support
from test.support import import_helper, script_helper

#
# Define some utility functions
#


def create_temp_c_file(content, dir=None):
    # Create a temp file, write 'content' to it, and return a
    # (file, filename) pair.  The file is opened for reading and writing,
    # and will be automatically deleted when it is closed (in either
    # case, explicitly or by garbage collection).  'content' may be either
    # a string or a byte string.
    if dir is None:
        dir = tempfile.gettempdir()
    fd, name = tempfile.mkstemp(".c", "tmp", dir, True)
    file = os.fdopen(fd, "w+b")
    file.write(content)
    file.flush()
    return (file, name)


def create_test_module(module_name,
