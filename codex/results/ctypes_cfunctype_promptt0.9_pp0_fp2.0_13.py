import ctypes
# Test ctypes.CFUNCTYPE and ctypes.WINFUNCTYPE
import unittest
from test import support
# a function
def add_one(arg):
    return arg + 1
# a function type
DEFAULT_FUNCTYPE = ctypes.CFUNCTYPE if hasattr(ctypes, 'CFUNCTYPE') else ctypes.WINFUNCTYPE
# AFuncType for use in testing
AFuncType = DEFAULT_FUNCTYPE(ctypes.c_int, ctypes.c_int)
class TestCase(unittest.TestCase):

    @unittest.skip('hangs')
    def test_01_call_cfunc(self):
        """Call a ctypes function"""
        add_one = AFuncType(add_one)
        self.assertEqual(42, add_one(41))
        #
        # We can call the ctypes.CFunction directly
        #
        self.assertEqual(42, add_one.ctypes.CFunction(41))
        # Check the "restype" attribute
        self.assertEqual(add
