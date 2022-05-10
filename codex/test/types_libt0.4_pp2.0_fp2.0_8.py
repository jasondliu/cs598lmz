import types
types.ClassType = types.TypeType

import sys
import unittest

from test.test_support import run_unittest, check_syntax_error, check_py3k_warnings
import test.test_support

class TestSyntax(unittest.TestCase):

    def test_print(self):
        self.assertEqual(compile("print", "?", "single").co_stacksize, 1)
        self.assertEqual(compile("print >>", "?", "single").co_stacksize, 1)
        self.assertEqual(compile("print >>", "?", "single").co_flags & 4, 4)
        self.assertEqual(compile("print >>", "?", "single").co_flags & 8, 0)

    def test_print_to(self):
        self.assertEqual(compile("print >>", "?", "single").co_stacksize, 1)
        self.assertEqual(compile("print >>", "?", "single").co_flags & 4, 4)
        self.assertEqual
