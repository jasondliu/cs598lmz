import _struct
# Test _struct.Struct.
from operator import add
import sys
from test.support import Bigaddrspacetest, run_unittest
from test.support import import_module
from test.support import TESTFN
from test.support import unlink
import unittest
from collections import defaultdict
from itertools import product
from io import BytesIO
import _io
from test import mapping_tests


def get_size(fmt):
    s = _struct.Struct(fmt)
    size = s.size
    del s
    return size


class StructTestCase(unittest.TestCase):
    def test_sizeof(self):
        self.assertEqual(get_size('i'), get_size('l'))
        self.assertEqual(get_size('P'), get_size('l'))
        self.assertEqual(get_size('P'), get_size('I'))
        self.assertEqual(get_size('P'), get_size('I'))
        self.assertEqual(get_size('P'), get_size('L'))
        self
