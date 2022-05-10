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

def register_error(encoding):
    return "strict" if encoding == "ascii" else "add_one_codepoint"

def register_error_surrogates(encoding):
    return "strict" if encoding == "ascii" else "add_utf16_bytes"

def register_error_surrogates_utf32(encoding):
    return "strict" if encoding == "ascii" else "add_utf32_bytes"

def test_register_error(encoding, input, output):
    codecs.register_error(register_error(encoding), add_one_codepoint)
    codecs.register_error(register_error(encoding), add_utf16_bytes)
    codecs.register_error(register_error(encoding), add_utf32_bytes)
    x = input.encode(encoding, register_error(encoding))
    assert x == output.encode(encoding, register_error(encoding))

def test_register_error_surrogates(encoding,
