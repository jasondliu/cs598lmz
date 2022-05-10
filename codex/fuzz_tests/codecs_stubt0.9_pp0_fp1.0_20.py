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

print(ascii('\xc0').encode('utf-8', 'add_one_codepoint'))
print(ascii('\xc0').encode('utf-16', 'add_one_codepoint'))
print(ascii('\xc0').encode('utf-32', 'add_one_codepoint'))

print(ascii('\xc0').encode('utf-8', 'add_utf16_bytes'))
print(ascii('\xc0').encode('utf-16', 'add_utf16_bytes'))
print(ascii('\xc0').encode('utf-32', 'add_utf16_bytes'))

print(ascii('\xc0').encode('utf-8', 'add_utf32_bytes'))
print(ascii('\xc0').encode('utf-16', 'add_utf32_bytes'))
print(ascii('\xc0').encode('utf-32', 'add_utf32_bytes'))
