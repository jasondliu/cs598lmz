import _struct
# Test _struct.Struct
class TestStruct(unittest.TestCase):
    def test_unpack(self):
        # test unpack
        with self.assertRaises(struct.error):
            _struct.Struct('c').unpack('abc')
        ret = _struct.Struct('c').unpack('a')
        self.assertEqual(ret, ('a',))
        with self.assertRaises(struct.error):
            _struct.Struct('cc').unpack('a')
        ret = _struct.Struct('cc').unpack('ab')
        self.assertEqual(ret, ('a', 'b'))
        # more tests
        ret = _struct.Struct('i').unpack(_struct.pack('i', 123))
        self.assertEqual(ret, (123,))
        # more tests
        ret = _struct.Struct('if').unpack(_struct.pack('if', 123, 456.0))
        self.assertEqual(ret, (123, 456.0))
        self.assertEqual(_struct.Struct('c').size, 1)
       
