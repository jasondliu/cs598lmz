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

# UTF-16

b = b'\xff\xfe\xd8\x00\xdc\x00'
u = b.decode('utf-16', 'add_one_codepoint')
assert u == '\U00010000'

b = b'\xff\xfe\xd8\x00\xdc\x00\x1f'
u = b.decode('utf-16', 'add_one_codepoint')
assert u == '\U00010000\udc1f'

b = b'\xff\xfe\xd8\x00\xdc\x00\x1f\x00'
u = b.decode('utf-16', 'add_one_codepoint')
assert u == '\U00010000\udc1f'

b = b'\xff\xfe\xd8\x00\xdc\x00\x1f\x00\x1f'
u = b.decode('utf-16', 'add_one_codepoint')
assert u == '\U
