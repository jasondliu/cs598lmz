import ctypes
# Test ctypes.CFUNCTYPE.
#
# See ctypes/test/test_cfunctype.py for more tests.

import sys

if sys.platform == "darwin":
    import platform
    ver = platform.mac_ver()
    if ver[0][:4] == "10.5":
        # ctypes can't handle the __pyx_convert_<type>_to_py functions
        # on MacOS X 10.5 (and maybe 10.4)
        raise SystemExit

from ctypes import *
import unittest

class CFUNCTYPE_TestCase(unittest.TestCase):
    def check_error(self, errcls, errobj, func, args):
        try:
            func(*args)
        except errcls as e:
            self.assertIs(errobj, e)
        else:
            self.fail("%s not raised" % errcls.__name__)

    def test_argtypes_restrictions(self):
        if sizeof(c_char_p) != sizeof(c_void_p
