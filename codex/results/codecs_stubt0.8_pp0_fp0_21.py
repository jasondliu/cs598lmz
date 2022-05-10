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

#
#   Encode
#
def test_encode_error_handling(encoding):
    # error handler that adds one code point
    for errors in ["strict", "ignore", "replace", add_one_codepoint]:
        # invalid code point
        inp = "b\udce2\udce3\udc00"
        try:
            codecs.encode(inp, encoding, errors)
        except UnicodeEncodeError as e:
            pass
        else:
            if errors == "strict":
                raise AssertionError("encoding didn't raise UnicodeEncodeError")
            elif errors == "ignore":
                raise AssertionError("encoding didn't ignore U+DC00")
            elif errors == "replace":
                raise AssertionError("encoding didn't replace U+DC00")

    # error handler that adds UTF-16 bytes
    for errors in ["strict", "ignore", "replace", add_utf16_bytes]:
        # invalid code point
        inp = "b\udce2\udce3
