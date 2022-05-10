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

def test_decode_error_handling():
    # test decode error handling
    for encoding in ["ascii", "charmap", "iso8859-1", "iso8859-15", "macroman",
                     "utf-7", "utf-8", "utf-16", "utf-16-le", "utf-16-be",
                     "utf-32", "utf-32-le", "utf-32-be"]:
        for errors in ["strict", "ignore", "replace", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"]:
            try:
                codecs.decode("abc\xffdef", encoding, errors)
            except UnicodeDecodeError:
                pass

def test_encode_error_handling():
    # test encode error handling
    for encoding in ["ascii", "charmap", "iso8859-1", "iso8859-15", "macroman",
                     "utf-7", "utf-8", "utf-16", "utf-16
