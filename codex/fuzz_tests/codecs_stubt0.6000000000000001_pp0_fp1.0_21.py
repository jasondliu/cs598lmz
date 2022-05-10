import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

from test import support

class TestUnicodeDecode(unittest.TestCase):

    def test_replace(self):
        # all possible error handling schemes:
        for errors in ('strict', 'ignore', 'replace', 'add_one_codepoint',
                       'add_utf16_bytes', 'add_utf32_bytes'):
            # all possible input types:
            for input in (bytes, bytearray, memoryview):
                self.check_decode_replace(input, errors)

    def check_decode_replace(self, input, errors):
        # unicode(input, errors='replace') replaces
        # all undecodable bytes with the default replacement character
        for i in range(256):
            b = bytes([i])
            if i == ord('\ufffd'):
                self.assertEqual(unicode(b, errors), u'\ufffd')
            else:
                self.assertEqual(unicode(b, errors), u'\ufffd')

        # unicode(input, errors='replace') replaces

