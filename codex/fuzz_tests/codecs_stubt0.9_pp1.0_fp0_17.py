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


class UnicodeTest():

    source = [
        (ord(x), "\\x%2.2x" % x) for x in range(0, 32)
    ]

    def test_str_decode(self):
        s = bytes(range(0, 256))
        u = s.decode(self.name)
        expected = "".join([x[-1] for x in self.source])
        self.assertEqual(u, expected)

    def test_str_encode(self):
        u = "".join([x[-1] for x in self.source])
        s = u.encode(self.name)
        expected = bytes(range(0, 32))
        self.assertEqual(s, expected)

    def test_unicode_decode(self):
        u = str(bytearray(range(0, 256)), "utf-8")
        s = u.encode("utf-8")
        u = s.decode(self.name, "add_one_codepoint")
        expected = "
