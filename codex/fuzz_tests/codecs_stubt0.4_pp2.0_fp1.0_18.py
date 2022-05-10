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
    # Test: UnicodeEncodeError
    for encoding in ["ascii", "utf-8", "utf-16", "utf-32"]:
        for error_handler in ["strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
            for unistr in [u"a\u1234", u"\u1234a", u"\u1234\u5678"]:
                try:
                    unistr.encode(encoding, error_handler)
                except UnicodeEncodeError:
                    pass

    # Test: UnicodeDecodeError
    for encoding in ["ascii", "utf-8", "utf-16", "utf-32"]:
        for error_handler in ["strict", "ignore", "replace"]:
            for bytestr in [b"a\x80", b"\x80a", b"\x80\x81"]:
                try:
                    bytestr.decode(encoding, error_
