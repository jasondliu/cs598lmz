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

def test_utf8_codec(decoding_error_handler, encoding_error_handler):
    # UTF-8 is a variable length encoding and thus is not a fixed-width encoding.
    with assert_raises(ValueError):
        codecs.lookup("utf-8")
    with assert_raises(ValueError):
        codecs.lookup("utf-8-sig")

    # UTF-8-sig is a fixed-width encoding with a BOM.
    assert_equal(codecs.lookup("utf-8-sig").encode("\u20ac", "replace")[0], b"\xef\xbb\xbf")
    assert_equal(codecs.lookup("utf-8-sig").encode("\u20ac", "replace")[1], b"\xe2\x82\xac")

    # UTF-8 is a variable length encoding and thus is not a fixed-width encoding.
    with assert_raises(ValueError):
        codecs.lookup("utf-8")

    # UTF-
