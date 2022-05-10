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

class TestUTF7(unittest.TestCase):

    def test_decoder_simple_add(self):
        self.assertEqual("\xFF+A-",
                         codecs.utf_7_decode("\xFF+A-", "replace")[0])
        self.assertEqual("\xFF+A-",
                         codecs.utf_7_decode("\xFF+A-", "ignore")[0])
        self.assertEqual("\xFFA",
                         codecs.utf_7_decode("\xFF+A-", "xmlcharrefreplace")[0])
        self.assertRaises(UnicodeDecodeError, codecs.utf_7_decode, "\xFF+A-")

        self.assertEqual("\xFF+A-",
                         codecs.utf_7_decode("\xFF+A-", "replace", state=bytes())[0])
        self.assertEqual(b"+AAA-",
                         codecs.utf_7_decode("+A-",
