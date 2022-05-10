import _struct
# Test _struct.Struct
#
# Test the _struct module.  This is a simple test, it only checks that
# the module is built correctly.  The _struct module is a C module,
# so it is tested by the test_builtin test suite.
#
# written by:    Fred L. Drake, Jr.
#                fdrake@acm.org
# last modified: March 25, 2002

import unittest
import _struct

class StructTest(unittest.TestCase):
    def test_format(self):
        self.assertEqual(_struct.Struct("").format, "")
        self.assertEqual(_struct.Struct("b").format, "b")
        self.assertEqual(_struct.Struct("bb").format, "bb")
        self.assertEqual(_struct.Struct("bbb").format, "bbb")
        self.assertEqual(_struct.Struct("bbbb").format, "bbbb")
        self.assertEqual(_struct.Struct("bbbbb").format, "bbbbb")
        self.assertEqual(_struct.Struct("bbbbbb
