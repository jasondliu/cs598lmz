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
    # Test UTF-16 surrogate pairs
    for encoding in ("utf-16", "utf-16-be", "utf-16-le"):
        for errorhandler in ("strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes"):
            for data in (b'\xff\xfe\xd8\x00\xdc\x00', b'\x00\xd8\x00\xdc', b'\xd8\x00\xdc\x00'):
                try:
                    data.decode(encoding, errorhandler)
                except UnicodeDecodeError as e:
                    assert e.encoding == encoding
                    assert e.object == data
                    assert e.start == 0
                    assert e.end == len(data)
                    assert e.reason == "illegal UTF-16 surrogate"
                else:
                    assert errorhandler in ("replace", "ignore")

    # Test UTF-32 surrogate pairs
    for encoding in ("utf-32", "utf-32-be", "utf-32
