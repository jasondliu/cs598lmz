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
    with support.check_warnings(("", DeprecationWarning)):
        codecs.register_error("replace", codecs.replace_errors)

    # test codecs.strict_errors
    for encoding in ("ascii", "iso8859-1", "utf-8", "utf-16", "utf-32"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes", "add_utf32_bytes"):
            for input, expected in (
                (b"abc\xffdef", (b"abc?def", 3)),
                (b"abc\x80def", (b"abc\x80def", None)),
                (b"abc\x80def", (b"abc?def", 3)),
                (b"abc\x80def", (b"abc\x80def", None)),
                ):
                try:
                    result = codecs.decode(input, encoding, errors)
                except UnicodeDecodeError as e:

