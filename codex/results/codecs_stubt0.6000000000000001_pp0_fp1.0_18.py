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

# test UTF-16 codec

assert codecs.utf_16_encode(u'\U00023456') == (b'\x34\xd2\x56\x23', 4)
assert codecs.utf_16_encode(u'\U00023456', 'strict') == (b'\x34\xd2\x56\x23', 4)
assert codecs.utf_16_encode(u'\U00023456', 'ignore') == (None, 4)
assert codecs.utf_16_encode(u'\U00023456', 'replace') == (b'\xff\xfd', 2)
assert codecs.utf_16_encode(u'\U00023456', 'backslashreplace') == (b'\\U00023456', 10)
assert codecs.utf_16_encode(u'\U00023456', 'xmlcharrefreplace') == (b'&#23456;', 10)
assert codecs.utf_16_encode(u'\U00023456', 'add_one
