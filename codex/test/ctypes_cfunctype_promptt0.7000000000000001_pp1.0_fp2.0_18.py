import ctypes
# Test ctypes.CFUNCTYPE() with calling a nested function.
# Author: Andreas Stuhrk <andreas.stuhrk@simap.de>, 2008-04-08
#
# This test should not crash.
#
# Adapted by Martin v. Loewis to check that the call actually works.

import unittest

class CFuncTest(unittest.TestCase):

    def test(self):
        def func(a):
            return a

        func_type = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
        func_type(func)(2)

if __name__ == "__main__":
    unittest.main()
