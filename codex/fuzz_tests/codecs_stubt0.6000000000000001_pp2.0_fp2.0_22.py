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
    # test UTF-16 codec
    for enc in ("utf-16", "utf-16-be", "utf-16-le"):
        for bom in (b'', b'\xff\xfe', b'\xfe\xff'):
            for error in ("strict", "replace", "ignore", "add_one_codepoint",
                          "add_utf16_bytes"):
                for data in (b'\0\0', b'\0\0\0\0'):
                    # encode
                    s = data.decode("utf-16")
                    if bom:
                        s = s[1:]
                    e = codecs.getencoder(enc)
                    r, l = e(s, error)
                    if error != "strict":
                        if l != 1:
                            raise TestFailed("wrong length for '%s' with '%s' and '%s'" % (s, enc, error))
                        if error == "add_one_codepoint":
                            if r != bom + b'
