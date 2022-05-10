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

# Test with bytes
for enc in ('utf-8', 'utf-16-be', 'utf-16-le', 'utf-32-be', 'utf-32-le'):
    print('\n', enc, '\n')
    b = b'\xff'
    print(b.decode(enc, 'replace'))
    print(b.decode(enc, 'ignore'))
    print(b.decode(enc, 'backslashreplace'))
    print(b.decode(enc, 'xmlcharrefreplace'))
    print(b.decode(enc, 'add_one_codepoint'))
    print(b.decode(enc, 'add_utf16_bytes'))
    print(b.decode(enc, 'add_utf32_bytes'))

# Test with str
for enc in ('utf-8', 'utf-16-be', 'utf-16-le', 'utf-32-be', 'utf-32-le'):
    print('\n', enc, '\n')
    b = '
