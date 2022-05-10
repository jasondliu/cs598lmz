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

codecs.register_error("test.add_utf32_bytes", add_utf32_bytes)
codecs.register_error("test.add_one_codepoint", add_one_codepoint)

#
#   Encode/decode from/to Unicode
encoding = "utf-8"

def check_encode_decode(encoding, errors, input, expected_output):
    output = codecs.encode(input, encoding, errors)
    decoded_output = codecs.decode(output, encoding, errors)
    if input != decoded_output:
        raise Exception("decode+encode must be an identity")

    if output != expected_output:
        raise Exception("output must be %a, got %a" % (expected_output, output))

#   Simple encoding
input = "\x80"
expected_output = b'\xc2\x80'
check_encode_decode(encoding, "strict", input, expected_output)
check_encode_decode(encoding, "ignore",
