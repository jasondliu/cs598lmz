import codecs
# Test codecs.register_error()
from test.test_support import run_suite, check_impl_detail

from encodings import ascii, utf_7

class CodecsTest(unittest.TestCase):

    def test_utf8(self):
        if sys.platform == 'darwin':
            # Note: This is a stopgap until UTF-8 support is
            # improved on OSX
            raise unittest.SkipTest('UTF-8 does not have fixed width on OSX')
        for i in range(0x100):
            self.assertEqual(codecs.utf_8_encode(chr(i))[0], chr(i).encode('utf-8'))
            self.assertEqual(codecs.utf_8_decode(chr(i).encode('utf-8'))[0], chr(i))
            self.assertEqual(codecs.charbuffer_encode(chr(i))[0], chr(i).encode('utf-8'))
            self.assertEqual(codecs
