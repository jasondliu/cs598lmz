import codecs
# Test codecs.register_error('ignore', 'codecs.ignore_errors')
import imp

class TestCodeFunctions(unittest.TestCase):

    def test_decoding(self):
        # Testing the byte-to-string codec APIs
        self.assertEqual(codecs.escape_decode(b'abc'), ('abc', 3))
        self.assertEqual(codecs.escape_decode(b'abc\n'), ('abc\n', 5))
        self.assertEqual(codecs.escape_decode(b'ab\\c'), ('abc', 5))
        self.assertEqual(codecs.escape_decode(b'ab\\x00c'), ('ab\x00c', 7))
        self.assertEqual(codecs.escape_decode(b'ab\\077c'), ('abc', 7))
        self.assertEqual(codecs.escape_decode(b'ab\\x1fc'), ('ab\x1fc', 7))
        self.assertEqual(codecs.escape_decode(b'ab\\
