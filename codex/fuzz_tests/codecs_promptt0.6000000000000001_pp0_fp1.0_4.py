import codecs
# Test codecs.register_error()

def search_function(encoding):
    if encoding != "test.unicode":
        return None
    def encode(input, errors="strict"):
        return (input.encode("utf-8"), len(input))
    def decode(input, errors="strict"):
        return (input.decode("utf-8"), len(input))
    return codecs.CodecInfo(encode, decode, name="test.unicode")

codecs.register(search_function)
import test.test_support

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

class Test_Unicode(unittest.TestCase):
    maxDiff = None

    def test_1(self):
        self.assertEqual(u'\ud800', '\ud800')
        self.assertEqual(u'\ud800', '\ud800'.decode('utf-8'))
        self.assertEqual(u'\ud800', '\ud800'.decode('utf-8
