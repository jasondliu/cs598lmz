import _struct
# Test _struct.Struct.

from test import string_tests
from test import support
import sys

struct_types = ['x', 'c', 'b', '?', 'h', 'i', 'l', 'q', 'f', 'd']
if hasattr(sys, 'longlong'):
    struct_types.append('Q')
if hasattr(sys, 'longdouble'):
    struct_types.append('g')

# Needed so the test can be run without -A on Python 3.2
def string_from_buffer_copy(*args, **kwargs):
    return bytes(args[0])

class StructTest(unittest.TestCase):

    def test_internal_sizeof(self):
        st = _struct.Struct('hhl')
        self.assertEqual(st.size, st.__sizeof__())
        self.assertEqual(st.size, st._sizeof())
        self.assertEqual(st.size, st.internal_sizeof())
        st = _struct.Struct('hhlxxxx')
        self.assertEqual(st.
