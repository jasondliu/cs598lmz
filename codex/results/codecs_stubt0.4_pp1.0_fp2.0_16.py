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
    import sys, codecs, StringIO

    #
    # UTF-16
    #

    # encode
    s = "abcd"
    for encoding in ["utf-16", "utf-16-le", "utf-16-be"]:
        for errors in ["strict", "replace", "ignore", "add_one_codepoint",
                       "add_utf16_bytes"]:
            f = StringIO.StringIO()
            f.write(s.encode(encoding, errors))
            f.seek(0)
            t = f.read().decode(encoding, errors)
            if encoding.endswith("-le"):
                assert t == "abcd\ufffd"
            else:
                assert t == "\ufffdabcd"

    # decode
    s = b"\xff\xfea\x00b\x00c\x00d\x00"
    for encoding in ["utf-16", "utf-16-le", "utf-16-be"]:
        for errors in ["st
