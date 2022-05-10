import _struct
# Test _struct.Struct class method center - Issue #12145
import _struct as struct
from _struct import Struct
from test import support
# Issue 14762 - Cannot pass unicode format strings to struct
from test.support import run_unittest


class StructTest(unittest.TestCase):

    def test_args(self):
        struct._clearcache()
        s = struct.Struct('x')
        self.assertEqual(repr(s), "<class '_struct.Struct'>")
        self.assertEqual(struct.Struct.format, 'x')
        self.assertEqual(struct.Struct.size, 1)
        self.assertIsInstance(struct.Struct.format, str)
        self.assertIsInstance(struct.Struct.size, int)
        s2 = struct.Struct(b'x')
        self.assertEqual(s.format, s2.format)
        self.assertEqual(s.size, s2.size)
        s3 = struct.Struct(u'x')
        self.assertEqual(s.format, s3.format)
       
