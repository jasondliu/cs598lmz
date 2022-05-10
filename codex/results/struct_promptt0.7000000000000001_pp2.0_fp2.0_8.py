import _struct
# Test _struct.Struct.unpack error handling
import _testcapi
import unittest

class StructTest(unittest.TestCase):
    def test_iter_unpack(self):
        St = _struct.Struct(b'i')
        self.assertRaises(RuntimeError, iter, St.iter_unpack(b''))

    def test_unpack_from_iterable(self):
        St = _struct.Struct(b'ii')
        self.assertRaises(TypeError, St.unpack_from, (1,))

    def test_pack_iterable(self):
        class BadIterable:
            def __iter__(self):
                return self
            def __next__(self):
                raise RuntimeError
            def __length_hint__(self):
                return 1
        St = _struct.Struct(b'i')
        self.assertRaises(RuntimeError, St.pack, BadIterable())

    def test_iter_unpack_from(self):
        St = _struct.Struct(b'i')
        self.assertRaises(
