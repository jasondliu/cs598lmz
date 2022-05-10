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

def test_utf8_decode_error(self):
    import _codecs
    for encoding in ("utf-8", "utf_8"):
        for errorhandler in ("strict", "replace", "ignore"):
            for text in (b"\xff", b"\xff\xff", b"\xff\xff\xff"):
                with self.assertRaises(UnicodeDecodeError):
                    _codecs.utf_8_decode(text, errors=errorhandler)
        for errorhandler in ("add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
            for text, expected in [(b"\xff", "a"), (b"\xff\xff", "a"), (b"\xff\xff\xff", "a")]:
                self.assertEqual(
                    _codecs.utf_8_decode(text, errors=errorhandler),
                    (expected, len(text))
                )

def test_utf16_decode_error(self):
    import _codec
