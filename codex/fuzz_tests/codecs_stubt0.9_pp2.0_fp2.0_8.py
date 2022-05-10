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

s = '\u0430\u0441'

print('unicode -> utf32')
print(s.encode('utf32'))
print(s.encode('utf32', 'replace'))
print(s.encode('utf32', 'surrogateescape'))
print(s.encode('utf32', 'surrogateescape'), 'replace')

print(s.encode('utf32', 'add_one_codepoint'))
print(s.encode('utf32', 'add_utf16_bytes'))
print(s.encode('utf32', 'add_utf32_bytes'))

print('unicode -> utf16')
print(s.encode('utf16'))
print(s.encode('utf16', 'replace'))
print(s.encode('utf16', 'surrogateescape'))
print(s.encode('utf16', 'surrogateescape'), 'replace')

print(s.encode('utf16', 'add_one_codepoint'))
print(s.
