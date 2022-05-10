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

# utf-16-le

encode_hints = {'errors': 'replace'}

expect = b'A\x00\xff\xff\uffff\x00\xff'

assert codecs.utf_16_le_encode(b'A\xff\uffff\xff', **encode_hints)[0] == expect

assert codecs.utf_16_le_encode(b'A\xff\xff\xff', **encode_hints)[0] == expect

assert codecs.utf_16_le_encode(b'A\xff\xff\xff', **encode_hints)[0] == expect

# utf-16-be

expect = b'\xff\xfeA\x00\x00\xff\xff\x00\xff'

assert codecs.utf_16_be_encode(b'\xff\xffA\xff', **encode_hints)[0] == expect

assert codecs.utf_16_be_encode(b'\xff\xff\xff
