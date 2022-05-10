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

