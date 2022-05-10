import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test_codecs_ignore_errors(unittest.TestCase):

    def test_decode(self):
        self.assertEqual(codecs.ignore_errors.decode('abc', 'strict'),
                         ('abc', 3))
        self.assertEqual(codecs.ignore_errors.decode('abc\xff', 'strict'),
                         ('abc\ufffd', 4))
        self.assertEqual(codecs.ignore_errors.decode('abc\xff', 'strict', True),
                         ('abc\ufffd', 4))
        self.assertEqual(codecs.ignore_errors.decode('abc\xff', 'strict', False),
                         ('abc\ufffd', 4))
        self.assertEqual(codecs.ignore_errors.decode('abc\xff', 'strict', None),
                         ('abc\ufffd', 4))

    def test_encode(self):
        self.assertEqual(codecs.ignore_
