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

def test_add_one_codepoint(encoding):
    "Tests that adding a single code point works in the given codec."

    codec_info = codecs.lookup(encoding)
    assert codec_info.name == encoding
    name = codec_info.name
    if name == "utf-16":
        # This is always little-endian.
        name = "utf-16-le"
    elif name == "utf-32":
        # This is always big-endian.
        name = "utf-32-be"

    assert b"abc\xff".decode(name) == "abc\uFFFD"
    assert b"abc\xff".decode(name, "add_one_codepoint") == "abca"
    # 'utf-16' is special-cased in CPython:
    if encoding == "utf-16":
        assert b"a\x00\xffb".decode(name) == "a\uFFFDb"
        assert b"a\x00\xffb".decode(name, "
