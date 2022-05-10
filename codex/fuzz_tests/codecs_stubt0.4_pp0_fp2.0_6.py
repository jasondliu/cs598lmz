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

# test utf-8
for enc in ["utf-8", "utf_8"]:
    try:
        u"\U0010FFFF".encode(enc)
    except UnicodeEncodeError as exc:
        assert exc.reason == "surrogates not allowed"
        assert exc.object == "\U0010FFFF"
        assert exc.start == 0
        assert exc.end == 1
        assert exc.encoding == enc
        assert exc.args == ("surrogates not allowed", "\U0010FFFF", 0, 1, enc)
        assert str(exc) == "'utf-8' codec can't encode character '\\U0010ffff' in position 0: surrogates not allowed"
    else:
        assert False, "should have raised UnicodeEncodeError"
    assert u"\U0010FFFF".encode(enc, "replace") == b"?"
    assert u"\U0010FFFF".encode(enc, "backslashreplace") == b"\\U0010ffff"
    assert u"\U0010FFFF".encode(enc, "xmlcharrefreplace") == b"&#
