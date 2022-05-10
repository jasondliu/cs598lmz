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

def test(utf16_bytes, utf32_bytes, encoding, error_handler):
    decoded_utf16 = utf16_bytes.decode(encoding, errors="surrogatepass")
    encoded_utf16 = decoded_utf16.encode(encoding, errors=error_handler)
    if encoded_utf16 != utf16_bytes:
        print("utf16: %s != %s" % (utf16_bytes, encoded_utf16))
    decoded_utf32 = utf32_bytes.decode(encoding, errors="surrogatepass")
    encoded_utf32 = decoded_utf32.encode(encoding, errors=error_handler)
    if encoded_utf32 != utf32_bytes:
        print("utf32: %s != %s" % (utf32_bytes, encoded_utf32))

test(b'\xed\xb0\x80', b'\x00\x00\x00\x00', 'utf-16-be', "add_one_codepoint")
test(b
