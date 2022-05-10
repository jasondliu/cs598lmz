import _struct
# Test _struct.Struct class.

import unittest
import sys
import io
import _testcapi


class StructTest(unittest.TestCase):

    def test_format_size(self):
        format_size_tests = [('xx','<','c','c','b'),
                             ('xxxx','=','h','h','h'),
                             ('x','@','b','B','B'),
                             ('xxxxx','>','i','i','i'),
                             ('x','!','b','B','B'),
                             ]
        for code, expected in format_size_tests:
            self.assertEqual(_struct.calcsize(code),expected)

        for code, *dummy in format_size_tests:
            self.assertEqual(_struct.calcsize(code),_struct.calcsize(code),
                             'calcsize("{}") != calcsize("{}")'.format(code,code))

    def test_calcsize(self):
        calcsize_tests = [('x', 1),
                          ('c', 1),

