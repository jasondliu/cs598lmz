import types
types.ClassType = type
types.MethodType = type

import types
try:
    types.UnboundMethodType = types.MethodType
except AttributeError:
    pass

try:
    import unittest2 as unittest
except ImportError:
    import unittest

import sys
if sys.version_info >= (2, 7):
    import unittest
    unittest.skip = unittest.skip
else:
    # python 2.6
    import unittest2 as unittest
    unittest.skip = unittest.skipIf

import os
try:
    os.unlink('/tmp/bdr_test_file')
except OSError as e:
    if e.errno != 2:  # No such file or directory
        raise

import random
import shutil
import tempfile
import time

import drbdmanage.config as config
import drbdmanage.consts as consts
import drbdmanage.exceptions as dmexc
import drbdmanage.utils as utils
from dr
