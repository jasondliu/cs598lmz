import codecs
# Test codecs.register_error
import test_codecs

class CodecsModuleTest(unittest.TestCase):
    # Test codecs.getreader/writer()
    def test_getreader(self):
        self.assertRaises(TypeError, codecs.getreader, 1)
        self.assertRaises(TypeError, codecs.getreader, 'c', 1)
        self.assertRaises(TypeError, codecs.getreader, 'c', io.BytesIO(), 1)
        self.assertRaises(LookupError, codecs.getreader, 'xxx')
        self.assertRaises(LookupError, codecs.getreader, 'xxx', None)

        reader = codecs.getreader('utf-8')
        self.assertEqual(reader('\xe2\x98\x83'.encode('utf-8')), '\u2603')

        f = io.BytesIO()
        f.write('\xe2\x98\x83')
        f.seek(0)
        reader = codecs.getreader('utf-8')
        self.
