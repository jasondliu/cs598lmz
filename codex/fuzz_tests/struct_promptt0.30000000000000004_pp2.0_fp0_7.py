import _struct
# Test _struct.Struct
import _struct

class TestStruct(unittest.TestCase):

    def test_format_sizeof(self):
        self.assertEqual(_struct.calcsize('i'), 4)
        self.assertEqual(_struct.calcsize('ii'), 8)
        self.assertEqual(_struct.calcsize('i'*1000), 4000)
        self.assertEqual(_struct.calcsize('i'*1000 + 'f'*2000), 8000)
        self.assertEqual(_struct.calcsize('i'*1000 + 'f'*2000 + 'd'*3000), 16000)
        self.assertEqual(_struct.calcsize('i'*1000 + 'f'*2000 + 'd'*3000 + 'h'*4000), 20000)
        self.assertEqual(_struct.calcsize('i'*1000 + 'f'*2000 + 'd'*3000 + 'h'*4000 + 'c'*5000), 25000)
        self.assertEqual(_struct.calcsize('i'*1000 + 'f'*
