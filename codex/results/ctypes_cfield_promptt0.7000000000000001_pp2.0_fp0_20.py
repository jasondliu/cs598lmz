import ctypes
# Test ctypes.CField class
# This test is not run from a script
#
# one of the following should work:
#  $ make -k test
#  $ make -k test TESTOPTS='-m "not bigendian"'
#  $ make -k test TESTOPTS='-m bigendian'
#
#  $ python -m test -m bigendian test_ctypes
import unittest
from test import support
from test.support import verbose, import_module
# Skip tests if _ctypes module doesn't exist.
ctypes = import_module('ctypes')
class CFUNCTYPE(ctypes.CFUNCTYPE):
    def __init__(self, *args):
        ctypes.CFUNCTYPE.__init__(self, *args)
        self.need_to_clear = False
        self._argtypes_ = args[:-1]
    def __call__(self, *args):
        if not self.need_to_clear:
            self.need_to_clear = True
            self._flags_ = (self._flags_ & ~ct
