import _struct
# Test _struct.Struct.format_size()

class TestFormatSize(unittest.TestCase):

    def test_format_size(self):
        self.assertEqual(_struct.Struct('i').format_size('<'), 4)
        self.assertEqual(_struct.Struct('i').format_size('>'), 4)
        self.assertEqual(_struct.Struct('i').format_size('@'), 4)
        self.assertEqual(_struct.Struct('i').format_size('!'), 4)
        self.assertEqual(_struct.Struct('q').format_size('<'), 8)
        self.assertEqual(_struct.Struct('q').format_size('>'), 8)
        self.assertEqual(_struct.Struct('q').format_size('@'), 8)
        self.assertEqual(_struct.Struct('q').format_size('!'), 8)
        self.assertEqual(_struct.Struct('P').format_size('<'), _struct.calcsize('P'))
