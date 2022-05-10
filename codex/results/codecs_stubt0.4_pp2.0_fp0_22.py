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
    for encoding in ["utf-8", "utf-16", "utf-32"]:
        for error_handler in ["strict", "ignore", "replace", "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]:
            f = open("test_codecs_%s_%s.txt" % (encoding, error_handler), "wb")
            f.write(b'\x80')
            f.close()
            f = open("test_codecs_%s_%s.txt" % (encoding, error_handler), "r", encoding=encoding, errors=error_handler)
            f.read()
            f.close()
            f = open("test_codecs_%s_%s.txt" % (encoding, error_handler), "rb")
            f.read()
            f.close()
            os.remove("test_codecs_%s_%s.txt" % (encoding, error_handler))

test_main()
