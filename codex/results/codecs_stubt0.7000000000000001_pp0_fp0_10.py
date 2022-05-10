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

# With surrogateescape, we should be able to decode any byte sequence
# without an error.

utf8_decoder = codecs.getincrementaldecoder("utf-8")()
utf8_decoder.set_error_handler(codecs.surrogateescape)

for i in range(0x10000):
    encoded = bytes((i,))
    decoded, consumed = utf8_decoder.decode(encoded, final=True)
    assert consumed == 1
    encoded_back = decoded.encode("utf-8", "surrogateescape")
    assert encoded == encoded_back

# With surrogatescape, we should be able to encode any Unicode string
# without an error.

utf8_encoder = codecs.getincrementalencoder("utf-8")()
utf8_encoder.set_error_handler(codecs.surrogateescape)

for i in range(0x10000):
    encoded = bytes((i,))
    decoded = chr(i)
    encoded_back = utf8_enc
