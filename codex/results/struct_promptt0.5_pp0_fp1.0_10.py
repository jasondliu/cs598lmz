import _struct
# Test _struct.Struct.format_size()

import sys
import unittest
from test import support

class TestStruct(unittest.TestCase):

    def test_format_size(self):
        def check(fmt, size):
            self.assertEqual(_struct.Struct(fmt).format_size(fmt), size)
        check('=', 0)
        check('<', 0)
        check('>', 0)
        check('!', 0)
        check('=b', 1)
        check('<b', 1)
        check('>b', 1)
        check('!b', 1)
        check('=B', 1)
        check('<B', 1)
        check('>B', 1)
        check('!B', 1)
        check('=h', 2)
        check('<h', 2)
        check('>h', 2)
        check('!h', 2)
        check('=H', 2)
        check('<H', 2)
        check('>H', 2)
        check('!H', 2)
        check
