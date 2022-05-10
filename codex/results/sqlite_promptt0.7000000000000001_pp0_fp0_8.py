import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(':memory:')

import time

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# PyQt is not yet supported
# PyQt can not be tested properly due to its license (GPL)

# Private imports
import _fsi

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Global settings

_debug = False

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Test functions

class _Test(object):

    def test_fsi_object(self):
        "Check the FSI object"
        fsi = _fsi.FSI()

    def test_fsi_constants(self):
        "Check FSI constants"
        fsi = _fs
