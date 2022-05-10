import _struct
# Test _struct.Struct()
import _struct
from test.support import _4G, run_unittest
from test import mapping_tests, string_tests, structseq_tests


class StructTestCase(unittest.TestCase):
    def test_struct(self):
        tests = structseq_tests.structseq_tests
        self.assertEqual(tests[0][1].format, 'c')
        self.assertEqual(tests[0][1].size, 1)
        self.assertEqual(tests[0][1].alignment, 1)
        self.assertEqual(tests[0][1].pack('x'), b'x')
        self.assertEqual(tests[0][1].pack(b'x'), b'x')
        self.assertEqual(tests[0][1].unpack(b'x'), (b'x',))
        self.assertEqual(tests[0][1].unpack_from(b'x', 0), (b'x',))
        self.assertEqual(tests[0][1].unpack_from(bytearray(
