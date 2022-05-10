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
    # test UnicodeEncodeError
    for encoding in ["ascii", "latin-1", "utf-8", "utf-16", "utf-32"]:
        for errorhandler in ["strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
            try:
                u"\u1234".encode(encoding, errorhandler)
            except UnicodeEncodeError:
                pass
            else:
                print("UnicodeEncodeError not raised with encoding %s and errorhandler %s" % (encoding, errorhandler))

    # test UnicodeDecodeError
    for encoding in ["ascii", "latin-1", "utf-8", "utf-16", "utf-32"]:
        for errorhandler in ["strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
            try:
                b"\xff".decode(encoding,
