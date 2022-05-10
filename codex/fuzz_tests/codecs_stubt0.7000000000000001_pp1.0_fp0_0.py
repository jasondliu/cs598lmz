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

utf_16_be = codecs.lookup('utf-16-be')
utf_32_be = codecs.lookup('utf-32-be')

# add_one_codepoint
assert u'????'.decode('utf-16-be', errors="add_one_codepoint") == u'\u0000a'
assert u'????'.decode('utf-32-be', errors="add_one_codepoint") == u'\U00000000a'

# add_utf16_bytes
assert u'????'.decode('utf-16-be', errors="add_utf16_bytes") == u'\u0000ab'
assert u'????'.decode('utf-32-be', errors="add_utf16_bytes") == u'\U00000000ab'

# add_utf32_bytes
assert u'????'.decode('utf-16-be', errors="add_utf32_bytes") == u'\U00000004abcd'
assert u'????'.decode('utf-32-be', errors="add_utf32_bytes")
