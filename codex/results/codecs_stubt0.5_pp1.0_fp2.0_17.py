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

def test_utf8_decode(self):
    self.assertEqual(b"abc".decode("utf-8", "add_one_codepoint"), u"aabc")
    self.assertEqual(b"abc".decode("utf-16", "add_utf16_bytes"), u"aabc")
    self.assertEqual(b"abc".decode("utf-32", "add_utf32_bytes"), u"aabc")

def test_utf8_encode(self):
    self.assertEqual(u"abc".encode("utf-8", "add_one_codepoint"), b"aabc")
    self.assertEqual(u"abc".encode("utf-16", "add_utf16_bytes"), b"aabc")
    self.assertEqual(u"abc".encode("utf-32", "add_utf32_bytes"), b"aabc")

def test_utf8_decode_errors(self):
    self.assertEqual(b"\xff".decode("utf-8",
