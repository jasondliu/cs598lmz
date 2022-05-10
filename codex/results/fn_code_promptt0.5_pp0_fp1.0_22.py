fn = lambda: None
# Test fn.__code__.co_firstlineno and fn.__code__.co_filename
#
# Note: This test is not intended to be run in a multi-threaded
# environment.

import sys
import unittest
from test import support

class TestCo(unittest.TestCase):
    def test_co_firstlineno(self):
        self.assertEqual(TestCo.test_co_firstlineno.__code__.co_firstlineno,
                         sys._getframe().f_lineno - 1)

    def test_co_filename(self):
        self.assertEqual(TestCo.test_co_filename.__code__.co_filename,
                         __file__.replace('.pyc', '.py'))

def test_main():
    support.run_unittest(TestCo)

if __name__ == "__main__":
    test_main()
