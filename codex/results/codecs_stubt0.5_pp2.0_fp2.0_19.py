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

def test_utf16_be_decode_error_handling(self):
    utf16_be = codecs.getdecoder("utf-16-be")
    self.assertEqual(utf16_be(b'\xff', "replace")[0], '\ufffd')
    self.assertEqual(utf16_be(b'\xff', "ignore")[0], '')
    self.assertEqual(utf16_be(b'\xff', "add_one_codepoint")[0], 'a')
    self.assertEqual(utf16_be(b'\xff', "add_utf16_bytes")[0], 'ab')
    self.assertEqual(utf16_be(b'\xff', "add_utf32_bytes")[0], 'abcd')

def test_utf16_le_decode_error_handling(self):
    utf16_le = codecs.getdecoder("utf-16-le")
    self.assertEqual(utf16_le(b'\xff', "replace
