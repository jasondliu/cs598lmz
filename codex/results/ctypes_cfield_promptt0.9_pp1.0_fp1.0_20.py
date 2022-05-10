import ctypes
# Test ctypes.CField() constructor 
import datetime
import os
import unittest
import test.support
import sys

try:
    unicode
except NameError:
    # Python 3.x
    basestring = unicode = str

# Where the test data files are.
NFILES = 3
FDATA_PATH = os.path.join(os.path.dirname(__file__), 'fdatas')
if sys.platform == 'darwin':
    FDATA_FORMAT = os.path.join(FDATA_PATH, 'pthread_%d')
else:
    FDATA_FORMAT = os.path.join(FDATA_PATH, 'fdata%d')

try:
    nt
except NameError:
    # Don't test non-unicode fields on non-Windows platforms.
    FDATA_FORMAT = os.path.join(FDATA_PATH, 'fdata%dW')
    try:
        unicode('').encode('mbcs')
    except LookupError:
        FDATA_FORMAT = None
    else:
       
