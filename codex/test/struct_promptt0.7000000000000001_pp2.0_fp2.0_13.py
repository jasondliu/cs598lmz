import _struct
# Test _struct.Struct.


try:
    from _testcapi import set_error_class
except ImportError:
    # Python compiled without the _testcapi module.
    def set_error_class(klass):
        pass

import test.support

class StructTest(unittest.TestCase):

    def test_unpack(self):
        x = struct.pack('hhl', 1, 2, 3)
        self.assertEqual(struct.unpack('hhl', x), (1, 2, 3))

    def test_iter_unpack(self):
        x = struct.pack('hhl', 1, 2, 3)
        self.assertEqual(tuple(struct.iter_unpack('hhl', x)), ((1, 2, 3),))

    def test_pack_into(self):
        x = bytearray(struct.calcsize('hhl'))
        struct.pack_into('hhl', x, 0, 1, 2, 3)
