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
    # test utf-16
    for errors in ["strict", "replace", "ignore", "add_one_codepoint", "add_utf16_bytes"]:
        for byteorder in [">", "<"]:
            for bom in [True, False]:
                for data in ["abc", "ab\ud800", "ab\udc00", "ab\ud800\udc00"]:
                    if bom:
                        data = codecs.BOM_UTF16 + data.encode("utf-16" + byteorder)
                    else:
                        data = data.encode("utf-16" + byteorder)
                    if errors == "add_one_codepoint":
                        data += b'\x00'
                    elif errors == "add_utf16_bytes":
                        data += b'\x00\x00'
                    data = data.decode("utf-16" + byteorder, errors)
                    if errors == "add_one_codepoint":
                        assert data == "aabc"
                    elif errors == "add
