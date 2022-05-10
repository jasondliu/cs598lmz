import codecs
codecs.register_error('strict', codecs.ignore_errors)

#-------------------------------------------------------------------------------

class Test_codecs(unittest.TestCase):

    def test_bug1098990(self):
        # bug 1098990:  test codecs.escape_encode() and
        # codecs.escape_decode()
        self.assertEqual(codecs.escape_decode(b'abc'), (b'abc', 3))
        self.assertEqual(codecs.escape_decode(b'\\x61bc'), (b'abc', 5))
        self.assertEqual(codecs.escape_decode(b'\\U00000061bc'), (b'abc', 11))
        self.assertEqual(codecs.escape_decode(b'\\N{LATIN SMALL LETTER A}bc'),
                         (b'abc', 23))
        self.assertEqual(codecs.escape_decode(b'\\a\\b\\f\\n\\r\\t\\v\\\\'),
                         (b'\a\b\f\n\
