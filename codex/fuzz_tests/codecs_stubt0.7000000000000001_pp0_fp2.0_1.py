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

def test_unicode_decode_error_with_latin1_replace(self):
    # Issue #1602: Latin-1 codec should decode UnicodeDecodeError's
    # start and end attributes
    self.assertEqual(
        "\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd",
        unicode(u"\ufffd\ufffd\ufffd\ufffd\ufffd", "latin-1", "replace"))
    self.assertEqual(
        "\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd\xef\xbf\xbd",
        unicode(u"\ufffd\ufffd\ufffd\ufffd\ufffd", "latin-1", "replace"))
    self.assertEqual(
        "\xef\xbf\xbd\xef\xbf\xbd\x
