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

# create test cases for the bytes and bytearray types.
for bytes_type in (bytes, bytearray):
    for encoding in ("utf-8", "utf-16", "utf-32"):
        for error_handler in ("strict", "replace", "ignore",
                              "add_one_codepoint", "add_utf16_bytes",
                              "add_utf32_bytes"):
            testcase = """
def test(self):
    encoding = {!r}
    error_handler = {!r}
    decoder = codecs.getincrementaldecoder(encoding)()
    bytes = {!r}
    decoder.decode(bytes, error_handler=error_handler)
    decoder.decode(bytes, error_handler=error_handler)
    """.format(encoding, error_handler, bytes_type([1, 2, 3]))
            exec(testcase)

if __name__ == "__main__":
    unittest.main()
