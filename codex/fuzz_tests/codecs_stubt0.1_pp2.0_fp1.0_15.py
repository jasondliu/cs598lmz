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
    # test utf-16-be
    for encoding in ("utf-16-be", "utf-16-le"):
        for errors in ("strict", "ignore", "replace", "add_one_codepoint",
                       "add_utf16_bytes"):
            for bom in (b"", b"\xff\xfe", b"\xfe\xff"):
                for data in (b"\x00\x00", b"\x00\x00\x00\x00"):
                    for i in range(len(data)):
                        for j in range(i, len(data)):
                            s = data[:i] + b"\xff" + data[j:]
                            try:
                                s.decode(encoding, errors)
                            except UnicodeDecodeError as exc:
                                if errors == "strict":
                                    pass
                                elif errors == "ignore":
                                    assert exc.end == i
                                elif errors == "replace":
                                    assert exc.end
