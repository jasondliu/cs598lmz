import mmap
import os
import sys
import time
import unittest

import pytest

from test import support
from test.support import TESTFN, run_unittest, unlink

# Skip this test if there is no bsddb module.
bsddb = support.import_module('bsddb')

# Skip this test if the bsddb module is too old.
if bsddb.version() < (4, 3, 0):
    raise unittest.SkipTest("bsddb module version too old")

# Skip this test if the bsddb module is too new.
if bsddb.version() >= (6, 0, 0):
    raise unittest.SkipTest("bsddb module version too new")

# Skip this test if the bsddb module is built without large file
# support.
if not hasattr(bsddb, 'DB_MPOOL_NOFILE'):
    raise unittest.SkipTest("bsddb module built without large file support")

# Skip this test if the bsddb module is built without
