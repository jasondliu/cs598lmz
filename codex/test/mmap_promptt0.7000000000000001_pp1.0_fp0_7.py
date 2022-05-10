import mmap
# Test mmap.mmap.
# TODO: Test readline() with mmap.mmap.
# TODO: Test writelines() with mmap.mmap.
import os
import pickle
import random
import re
import socket
import socket_helper
import sys
import tempfile
import test.test_support
import threading
import unittest
import weakref
import zipfile

from collections import namedtuple
from test.test_support import TESTFN, run_unittest, findfile, import_module, \
    verify, unlink, rmtree, findfile, check_warnings

# Filename used for testing
if os.path.exists(TESTFN):
    os.unlink(TESTFN)

# Disambiguate TESTFN for parallel testing, while letting it remain a valid
# module name.
TESTFN = "{}_{}_tmp".format(TESTFN, os.getpid())

# Make sure we can write to TESTFN
fp = file(TESTFN, 'w+')
fp.write('foo\n')
fp.close()

