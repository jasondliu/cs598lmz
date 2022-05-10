import ctypes
# Test ctypes.CFUNCTYPE and the ctypes callback mechanism
from ctypes import *
import unittest
from test import support


class CFunctionTypeTestCase(unittest.TestCase):
    def callback(self, *args):
        self.got_args = args
        return args[-1]

    def test_basic(self):
        CBFUNC = CFUNCTYPE(c_int, c_int, c_int)
        cb = CBFUNC(self.callback)
        result = cb(1, 2)
        self.assertEqual(result, 2)
        self.assertEqual(self.got_args, (1, 2))

#    def test_errcheck(self):
#        def errcheck(result, func, args):
#            self.assertEqual(args, (1, 2))
#            self.assertEqual(func.__name__, 'foobar')
#            self.assertEqual(result, 3)
#            return -result
#
#        CBFUNC = CFUNCTYPE(c_int, c_int,
