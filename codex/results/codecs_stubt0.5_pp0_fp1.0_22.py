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
    # Test unicode-escape
    encoded_text = b'\\u1234\\u5678'
    for encoding in ('unicode-escape', 'raw-unicode-escape'):
        decoded_text = encoded_text.decode(encoding)
        assert decoded_text == '\u1234\u5678'
        assert decoded_text.encode(encoding) == encoded_text

    # Test surrogatepass
    encoded_text = b'\xed\xa1\x8c\xed\xb2\x9c'
    for encoding in ('utf-16', 'utf-16-le', 'utf-16-be'):
        decoded_text = encoded_text.decode(encoding, 'surrogatepass')
        assert decoded_text == '\uD744\uDE1C'
        assert decoded_text.encode(encoding) == encoded_text

    # Test errors
    encoded_text = b'\xff'
    for encoding in ('utf-8', 'utf-
