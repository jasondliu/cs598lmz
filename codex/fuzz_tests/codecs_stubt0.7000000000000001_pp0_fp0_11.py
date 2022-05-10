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

# test error callback for encoding
def test_encode_callback():
    for encoding in ("ascii", "iso8859-1", "utf-8"):
        for errors in ("strict", "replace", "ignore", "add_one_codepoint"):
            for s in ("abc\xffde", "abc\xff\xffde", "abc\xff\xff\xffde"):
                try:
                    ascii(s)
                except UnicodeEncodeError:
                    pass
                else:
                    continue
                t = s.encode(encoding, errors)
                if errors == "strict":
                    raises(UnicodeEncodeError, ascii, s)
                elif errors == "replace":
                    assert ascii(t) == repr(t)
                elif errors == "ignore":
                    assert ascii(t) == repr(t[:3])
                elif errors == "add_one_codepoint":
                    assert ascii(t) == repr(t[:3] + b"a" + t[4
