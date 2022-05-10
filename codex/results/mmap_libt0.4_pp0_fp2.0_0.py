import mmap
import os
import re
import sys
import time
import traceback
import unittest

from test import support
from test.support import TESTFN, run_unittest, unlink, import_module

# Skip tests if there is no posix module.
posix = import_module('posix')

# Skip tests if there is no resource module.
resource = import_module('resource')

def get_attribute(obj, name):
    if name == 'st_atime_ns':
        return getattr(obj, name)
    if name == 'st_file_attributes':
        return getattr(obj, name)
    if name == 'st_birthtime_ns':
        return getattr(obj, name)
    if name == 'st_file_attributes_strings':
        return getattr(obj, name)
    if name not in dir(obj):
        raise unittest.SkipTest("attribute %s not available on this platform"
                                % name)
    else:
        return getattr(obj, name)

class PosixTester(
