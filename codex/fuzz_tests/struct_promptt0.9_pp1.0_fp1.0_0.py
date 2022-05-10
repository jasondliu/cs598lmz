import _struct
# Test _struct.Struct subclasses.
from test import support
try:
    import threading
except ImportError:
    threading = None
Struct = _struct.Struct

class StructSubclassTest(unittest.TestCase):
    def test_basic(self):
        class S(_struct.Struct):
            _fmt = 'i'
        s = S('i')
        self.assertEqual(s.size, _struct.calcsize('i'))
        self.assertEqual(S.size, _struct.calcsize('i'))
        self.assertEqual(s.pack(1), _struct.pack('i', 1))
        self.assertEqual(s.pack(1), S.pack(1))

    def test_buffer(self):
        class S(_struct.Struct):
            _fmt = 'i4s'
        s = S('i4s')
        self.assertEqual(S.size, _struct.calcsize('i4s'))
        self.assertEqual(s.pack(1, b'abcd'), _struct.
