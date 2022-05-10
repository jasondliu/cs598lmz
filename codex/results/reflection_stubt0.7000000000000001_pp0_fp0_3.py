fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_names = ("dummy",)
fn.__code__.co_filename = "dummy"
fn.__code__.co_firstlineno = 0
fn.__code__.co_lnotab = b"\x00\x01"

# issue: https://bugs.python.org/issue40499
# test: ./python -m test -v test_zipimport_support

import os
import sys
import zipimport
from test import support

try:
    import zlib
except ImportError:
    zlib = None

# For now, just run the test against the stdlib.
lib = sys.executable
STDLIB_TESTFN = os.path.join(os.path.dirname(lib), 'test_zipimport_support.py')
with open(STDLIB_TESTFN, 'rb') as stdlib_testfile:
    STDLIB_TESTDATA = stdlib_testfile.read()

# Helper to decompress a string.
if zlib:

