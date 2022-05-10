import _struct
# Test _struct.StructBin
class TestStructBin(unittest.TestCase):
    def test_from_struct(self):
        sf = _struct.StructBin._from_struct
        self.assertEqual(sf(struct.Struct('I')), _struct.StructBin('i', 4, '=', 'little'))
        self.assertEqual(sf(struct.Struct('4s')), _struct.StructBin('s', 4, '=', 'little'))
        self.assertEqual(sf(struct.Struct('>i')), _struct.StructBin('i', 4, '>', 'big'))
        self.assertEqual(sf(struct.Struct('>4s')), _struct.StructBin('s', 4, '>', 'big'))
        self.assertEqual(sf(struct.Struct('<i')), _struct.StructBin('i', 4, '<', 'little'))
        self.assertEqual(sf(struct.Struct('<4s')), _struct.StructBin('s', 4, '<', '
