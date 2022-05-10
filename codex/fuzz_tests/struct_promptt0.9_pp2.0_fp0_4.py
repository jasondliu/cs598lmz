import _struct
# Test _struct.Struct object.

support.valgrind_test()

class SwappedTest(unittest.TestCase):

    def test_swapped_basic(self):
        self.assertEqual(_struct.Struct('>').size,
                         _struct.Struct('>'.encode()).size)
        self.assertEqual(_struct.Struct('<').size,
                         _struct.Struct('<'.encode()).size)

    def test_swapped_special(self):
        self.assertEqual(_struct.Struct('@').size,
                         _struct.Struct('='.encode()).size)
        self.assertEqual(_struct.Struct('='.encode()).size,
                         _struct.Struct('@'.encode()).size)

class PackTest(unittest.TestCase):
    data = [ # (fmt, vals, result bytes), ... ]
        ('i', (1,), b'\x01\x00\x00\x00'),
        ('ii', (1,2), b'\x01\x00\x00\x
