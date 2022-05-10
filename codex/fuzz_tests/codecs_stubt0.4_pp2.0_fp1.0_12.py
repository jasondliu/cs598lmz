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

def test_main():
    for encoding in ("utf-8", "utf-16", "utf-32"):
        # test the default error handler
        try:
            u"\uDC80".encode(encoding)
        except UnicodeEncodeError as exc:
            assert exc.object == u"\uDC80"
            assert exc.encoding == encoding
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == "surrogates not allowed"
            assert exc.args == (u"\uDC80", 0, 1, "surrogates not allowed")
        else:
            assert False, "should have raised an exception"

        # test the replace error handler
        assert u"\uDC80".encode(encoding, "replace") == \
            ("?" if encoding == "utf-8" else b"?")

        # test the xmlcharrefreplace error handler
        assert u"\uDC80".encode(encoding, "xmlcharrefreplace") == \
            ("&#56320;" if encoding == "utf-
