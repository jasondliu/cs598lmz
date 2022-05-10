import mmap
# Test mmap.mmap

from test.support import TESTFN, findfile, unlink
from test.support import import_module
from test.script_helper import unindent, assert_python_ok

import warnings
warnings.filterwarnings('ignore', '.*mmap.mmap.* size is negative',
                        DeprecationWarning)

import sys
from os import path, fstat

from platform import architecture

from random import choice, randrange

from itertools import chain

from array import array
from cStringIO import StringIO
from tempfile import TemporaryFile

# try using the Windows read-only flag
try:
    mmap.ACCESS_READ
except AttributeError:
    mmap.ACCESS_READ = 0x1
else:
    mmap.ACCESS_COPY = 0xF

# create a file with a set of MS-DOS line endings
DOS_LINES = unindent("""
    line1^Z

    line2^Z

    line3^Z

    """).replace('\n', '\r\n')

def funused
