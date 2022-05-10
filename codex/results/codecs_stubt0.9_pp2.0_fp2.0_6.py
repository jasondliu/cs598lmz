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

with supports('wide') as utf16_decoder_name:
    source = b'\x00z'
    assert decode(utf16_decoder_name, source, "replace", True) == "z "
    assert decode(utf16_decoder_name, source, "add_one_codepoint") == "z a"
    source = b'\x00\x00z'
    assert decode(utf16_decoder_name, source, "replace", True) == " "
    assert decode(utf16_decoder_name, source, "add_utf16_bytes") == "ab"

with supports('wide') as utf32_decoder_name:
    source = b'\x00\x00\x00z'
    assert decode(utf32_decoder_name, source, "replace", True) == "z "
    assert decode(utf32_decoder_name, source, "add_one_codepoint") == "z a"
    source = b'\x00\x00\x00\x00z'
    assert
