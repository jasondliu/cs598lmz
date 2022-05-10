import mmap
import os
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import unittest

import pytest

from . import util
from . import test_support

# Skip these tests if there is no bz2 module.
bz2 = test_support.import_module('bz2')

TESTFN = test_support.TESTFN
TESTFN2 = TESTFN + "2"
TESTFNDIR = TESTFN + "d"
SMALL_SIZE = 10
FILE_SIZE = 10000

def _create_files():
    fp = open(TESTFN, 'wb')
    try:
        fp.write('I go out at 3 o clock for a quart of milk and come home at '
                 'five and then she is gone and I do not know where she has gone'
                 ' and so I must go out again.')
        fp.close()
        fp = open(TESTFN2, 'wb')
        fp.write('I go out at 3 o clock for a quart of milk and she is
