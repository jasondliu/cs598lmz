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

def test_decoding_U_state(self):
    s = b"\\\xFF"
    self.assertRaises(UnicodeDecodeError, s.decode, "unicode-escape")
    self.assertRaises(UnicodeDecodeError, s.decode, "unicode-escape", "strict")
    self.assertEqual(s.decode("unicode-escape", "ignore"), "")
    self.assertEqual(s.decode("unicode-escape", "replace"), "\\\ufffd")
    self.assertEqual(s.decode("unicode-escape", "add_one_codepoint"), "a")
    self.assertEqual(s.decode("unicode-escape", "add_utf16_bytes"), "\ufffd\ufffd")
    self.assertEqual(s.decode("unicode-escape", "add_utf32_bytes"), "\ufffd\ufffd")

def test_decoding_X_state(self):
    s = b"\\\xFF"
    self
