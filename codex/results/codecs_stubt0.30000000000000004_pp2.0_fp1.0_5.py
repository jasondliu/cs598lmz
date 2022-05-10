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
    # test surrogatepass
    for encoding in ("utf-8", "utf-16", "utf-32"):
        for errors in ("surrogatepass", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"):
            for data in (b'\xed\xa0\x80', b'\xed\xa0\x80\xed\xb0\x80'):
                for data_as_string in (True, False):
                    if data_as_string:
                        data = data.decode("latin-1")
                    try:
                        s = data.decode(encoding, errors)
                    except UnicodeDecodeError:
                        pass
                    else:
                        if errors == "surrogatepass":
                            assert s == '\udc80', (encoding, errors, data, s)
                        elif errors == "replace":
                            assert s == '\ufffd', (encoding, errors, data, s)
                        elif errors
