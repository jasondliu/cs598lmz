import _struct
# Test _struct.Struct and friends.
import copy
import os
import platform
import random
import sys
import unittest
import weakref
if sys.version_info[1] >= 6:
    # Python 2.6+
    e_prefix = b('!')
    import io
    import threading
    from test import test_support
else:
    e_prefix = ''
from test.test_support import run_unittest, import_module
NATIVE_PREFIX = e_prefix[:-1]

realstring = str
def b(s):
    return s.encode('latin-1')

def str_prefix(fmt):
    return not fmt.endswith(b('p'))

def bigendian(fmt):
    return fmt.startswith(b('>')) or fmt.startswith(b('!'))

# big-endian is false on non-big-endian platforms
# big-endian is never false on big-endian platforms
# true-big-endian is the same on all platforms
# byte_order is always true
