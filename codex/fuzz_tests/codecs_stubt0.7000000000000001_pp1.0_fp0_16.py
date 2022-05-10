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

def run_test(encoding, input, errors):
    # decode
    decoded, consumed = codecs.utf_32_le_decode(input, errors)
    print("decoded", repr(decoded), "consumed", consumed)

    # encode
    encoded, consumed = codecs.utf_32_le_encode(decoded, errors)
    print("encoded", repr(encoded), "consumed", consumed)

    # decode again
    decoded, consumed = codecs.utf_32_le_decode(encoded, errors)
    print("decoded", repr(decoded), "consumed", consumed)

run_test("utf-32-le", b'\x00\x00\x00\x00\x00\x00\x00\x00', "strict")
run_test("utf-32-le", b'\x00\x00\x00\x00\x00\x00\x00', "strict")
run_test("utf-32-le", b'\x00\x00\x00
