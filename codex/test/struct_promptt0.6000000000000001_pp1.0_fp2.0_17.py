import _struct
# Test _struct.Struct.unpack_from()

import array
from test import test_support

# Note: we're using array.array() instead of bytearray() or memoryview()
# because array.array() allows us to use the buffer interface.

class TestUnpackFrom(unittest.TestCase):
    def _test_unpack_from(self, format, data, expected_result,
                          expected_unpacked_bytes, offset=0):
        # Test with a bytearray
        a = array.array('B', data)
        st = _struct.Struct(format)
        result = st.unpack_from(a, offset)
        self.assertEqual(result, expected_result)
        self.assertEqual(st.size, expected_unpacked_bytes)

        # Test with a memoryview
        mv = memoryview(a)
        result = st.unpack_from(mv, offset)
        self.assertEqual(result, expected_result)
        self.assertEqual(st.size, expected_unpacked_bytes)

