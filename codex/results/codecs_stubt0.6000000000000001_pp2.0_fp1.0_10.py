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

def test_unicode_decode_error():
    u = chr(0xdc00) + chr(0xd800)
    for encoding in "utf-8", "utf-16", "utf-32":
        for errors in "strict", "replace", "ignore", "add_one_codepoint":
            u.encode(encoding, errors)

def test_unicode_encode_error():
    u = chr(0xdc00) + chr(0xd800)
    for encoding in "utf-8", "utf-16", "utf-32":
        for errors in "strict", "replace", "ignore":
            bytes(u, encoding, errors)
        for errors in "add_utf16_bytes", "add_utf32_bytes":
            try:
                bytes(u, encoding, errors)
            except UnicodeEncodeError as exc:
                assert exc.object == u
                assert exc.encoding == encoding
                assert exc.start == 1
                assert exc.end == 2
                assert exc.reason == "surrog
