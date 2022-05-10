fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
del gi

import marshal
import re
import struct
import sys
import time
import types
import zipfile

from test.test_support import verbose, TESTFN, import_module, unlink, \
    rmtree, cpython_only, run_unittest

def _create_test_zip():
    # List of files to be added to the ZIP file
    files = ['__init__.py', 'spam.py', 'bacon.py', 'ham.py']

    # Create the ZIP file
    zf = zipfile.ZipFile(TESTFN, 'w')
    try:
        # Create the file list
        for fname in files:
            zf.writestr(fname, '# test data: %s' % fname)
    finally:
        # Close the file
        zf.close()

class Trace:
    def __init__(self, count=0):
        self.count = count

    def __call__(self, *args):
        self.count += 1

# a mixin
