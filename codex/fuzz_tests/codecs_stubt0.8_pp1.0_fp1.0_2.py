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

def test_utf8_errors():
    errors = ["strict", "ignore", "replace", "xmlcharrefreplace", "backslashreplace",
              "add_one_codepoint", "add_utf16_bytes", "add_utf32_bytes"]

    for error in errors:
        codecs.register_error("test_utf8_" + error, codecs.lookup_error(error))
        for start in range(0, 6):
            for end in range(start, 6):
                for input in ["abc", b"abc", bytearray(b"abc")]:
                    d = codecs.getdecoder("utf8")(error="test_utf8_" + error)
                    s, consumed = d(input, start, end)
                    if input is b"abc" or type(input) is bytearray:
                        output = "abc"[start:end]
                    else:
                        output = "abc"
                    if error == "strict":
                        assert s == output
                        assert consumed == end - start
                    else:
                        assert s
