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

with TestCase('utf-16 surrogate handling') as test:
    test.assert_equals(codecs.utf_16_decode(b'\xff\xfe\x00\x00', errors='surrogate_or_strict')[0], '\u0000')
    test.assert_equals(codecs.utf_16_decode(b'\x00\x00', errors='surrogate_or_strict')[0], '\u0000')

with TestCase('utf-16 general handling') as test:
    test.assert_equals(codecs.utf_16_decode(b'\xff\xfe\x00\x00', errors='strict')[0], '\u0000')
    test.assert_equals(codecs.utf_16_decode(b'\x00\x00', errors='strict')[0], "\ufffd")

with TestCase('utf-16 surrogatepass handling') as test:
    test.assert_equals(codecs.utf_16_decode(
