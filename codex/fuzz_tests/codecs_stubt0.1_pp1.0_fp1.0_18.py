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
    # Test UTF-8
    for enc in ("utf-8", "utf_8"):
        for s in ("abc", "abc\u1234", "abc\u1234\u5678"):
            for errors in ("strict", "replace", "ignore", "add_one_codepoint"):
                for final in (True, False):
                    for bom in (True, False):
                        if bom:
                            s = codecs.BOM_UTF8 + s
                        if final:
                            s = s + "def"
                        for start in range(len(s) + 1):
                            for end in range(start, len(s) + 1):
                                for step in (-1, 1):
                                    try:
                                        x = s[start:end:step].encode(enc, errors)
                                    except UnicodeEncodeError:
                                        pass
                                    else:
                                        if errors == "strict":
                                            raise TestFailed("did not raise UnicodeEncodeError")
                                        if errors ==
