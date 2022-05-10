import _struct
# Test _struct.Struct

# Test _struct.Struct.__repr__
class TestRepr(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(struct.Struct('i')),
                         "Struct('i')")
        self.assertEqual(repr(struct.Struct('ci')),
                         "Struct('ci')")
        self.assertEqual(repr(struct.Struct('hi')),
                         "Struct('hi')")
        self.assertEqual(repr(struct.Struct('qi')),
                         "Struct('qi')")
        self.assertEqual(repr(struct.Struct('P')),
                         "Struct('P')")
        self.assertEqual(repr(struct.Struct('Pii')),
                         "Struct('Pii')")
        self.assertEqual(repr(struct.Struct('PiiP')),
                         "Struct('PiiP')")
        self.assertEqual(repr(struct.Struct('PiiPc')),
                         "Struct('PiiPc')")
