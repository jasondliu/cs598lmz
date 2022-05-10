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
    # test decoding
    for encoding in ('utf-8', 'utf-16', 'utf-32'):
        try:
            u"\uDC80".encode(encoding)
        except UnicodeEncodeError as exc:
            assert exc.object == u"\uDC80"
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == "surrogates not allowed"
            assert exc.encoding == encoding
            assert exc.object[exc.start:exc.end] == u"\uDC80"
        else:
            raise AssertionError("did not raise")

        # test encoding
        try:
            b"\x80".decode(encoding)
        except UnicodeDecodeError as exc:
            assert exc.object == b"\x80"
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == "invalid start byte"
            assert exc.encoding == encoding
            assert exc.object[exc.start:exc.end] == b
