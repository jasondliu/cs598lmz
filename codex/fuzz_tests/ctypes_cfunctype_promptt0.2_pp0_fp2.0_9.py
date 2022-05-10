import ctypes
# Test ctypes.CFUNCTYPE
#
# This test is based on the test_ctypes.py test_cfunctype test.
#
# The only difference is that the function is called with a
# different number of arguments.
#
# The bug was that the function was called with the wrong number
# of arguments, and the wrong number of arguments was passed to
# the function.

import unittest
from test import support

# The function to be called
def func(*args):
    return args

# The function type
FUNC = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# The function pointer
f = FUNC(func)

# The expected result
expected = (1, 2)

# The actual result
actual = f(1, 2)

# The test
class Test(unittest.TestCase):
    def test_call(self):
        self.assertEqual(actual, expected)

def test_main():
    support.run_unittest(Test)

if __name__
