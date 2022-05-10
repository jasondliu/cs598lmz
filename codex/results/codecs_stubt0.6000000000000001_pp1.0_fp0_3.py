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

class TestUTF8(unittest.TestCase):

    def test_utf8(self):
        u = chr(0x20ac)
        for i in range(1, len(u.encode("utf-8"))):
            data = u.encode("utf-8")[:i]
            self.assertRaises(UnicodeDecodeError, data.decode, "utf-8")
            self.assertEqual(data.decode("utf-8", "add_one_codepoint"), u)
            self.assertEqual(data.decode("utf-8", "replace"), "\ufffd")
            self.assertEqual(data.decode("utf-8", "ignore"), "")
            self.assertRaises(UnicodeEncodeError, u.encode, "utf-8", "add_one_codepoint")
            self.assertEqual(u.encode("utf-8", "replace"), data + b'\xef\xbf\xbd')
            self.assertEqual(u.encode("utf
