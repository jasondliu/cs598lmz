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

def test_utf16_le_decode(self):
    self.assertEqual(codecs.utf_16_le_decode(b"\xff\xfe\x00\x61\x00\x62"), ("ab", 2))
    self.assertEqual(codecs.utf_16_le_decode(b"\xff\xfe\x00\x61\x00\x62", "ignore"), ("ab", 2))
    self.assertEqual(codecs.utf_16_le_decode(b"\xff\xfe\x00\x61\x00\x62", "replace"), ("a\ufffd", 2))
    self.assertEqual(codecs.utf_16_le_decode(b"\xff\xfe\x00\x61\x00\x62", "backslashreplace"), ("a\\uFFFD", 2))
    self.assertEqual(codecs.utf_16_le_decode(b"\xff\xfe\x00\x61\x00
