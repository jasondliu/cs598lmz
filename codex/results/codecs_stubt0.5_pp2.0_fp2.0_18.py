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
    import sys
    if sys.maxunicode == 0xffff:
        # UCS2 build
        errors = ["add_one_codepoint", "add_utf16_bytes"]
    else:
        # UCS4 build
        errors = ["add_one_codepoint", "add_utf32_bytes"]
    for error in errors:
        for encoding in ["utf-8", "utf-16", "utf-32"]:
            for bad_string in ["\x80", "\x80\x80\x80", "\x80\x80\x80\x80"]:
                for bad_start in range(len(bad_string)):
                    for replacement in [u"", u"x"]:
                        try:
                            bad_string.encode(encoding, error)
                        except UnicodeError as exc:
                            try:
                                bad_string.encode(encoding, error,
                                                  replacement)
                            except UnicodeError as exc2:
                                assert exc.reason == exc2.reason
                                assert
