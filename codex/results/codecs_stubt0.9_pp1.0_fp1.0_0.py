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

class AbstractUnicodeCodecTest:

    def test_decode(self):
        eq = self.assertEqual
        eq(self.codec.decode(self.encoding), self.unicode)
        self.assertRaises(TypeError, self.codec.decode)
        eq(self.codec.decode(self.encoding, "strict"), self.unicode)
        eq(self.codec.decode(self.encoding, "ignore"), self.shortunicode)
        eq(self.codec.decode(self.encoding, "replace"),
           self.longunicode)
        eq(self.codec.decode(self.encoding, "xmlcharrefreplace"),
           self.xmldecode % self.longunicode)
        eq(self.codec.decode(self.encoding, "backslashreplace"),
           self.longunicode.encode("raw-unicode-escape"))
        eq(self.codec.decode(self.encoding, "add_one_codep
