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

def handle_utf16(error):
    return (u"", error.start)

def handle_utf32(error):
    return (u"", error.start)

codecs.register_error("handle_utf16", handle_utf16)
codecs.register_error("handle_utf32", handle_utf32)

def add_one_utf8(exc):
    return (b'', exc.start)

codecs.register_error("add_one_utf8", add_one_utf8)

# Test that decoding of UTF-8 with error handler that adds exactly one
# character produces the original Unicode string.
print(u'\U0010FFFF'.encode('utf-8').decode('utf-8', 'add_one_utf8'))

def identity(exc):
    return (exc.object[exc.start], exc.start+1)

codecs.register_error("identity", identity)

print(u'\U0010FFFF'.encode('utf-16-be').decode('utf-16-be
