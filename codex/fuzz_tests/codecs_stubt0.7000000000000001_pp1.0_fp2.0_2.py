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

class UnicodeErrorTest(unittest.TestCase):

    def test1(self):
        x = b'abcdabcd'
        self.assertEqual(
            codecs.decode(x, "utf-8", "replace"), "\ufffd\ufffd\ufffd\ufffd")
        self.assertEqual(
            codecs.decode(x, "utf-8", "ignore"), "")
        self.assertEqual(
            codecs.decode(x, "utf-8", "xmlcharrefreplace"), "&#65533;&#65533;")
        self.assertRaises(UnicodeError, codecs.decode, x, "utf-8", "strict")
        self.assertRaises(UnicodeError, codecs.decode, x, "utf-8")
        self.assertEqual(
            codecs.decode(x, "utf-8", "backslashreplace"), "\\xab\\xcd")
        self.assertRaises(UnicodeError, codecs.decode, x,
