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

def test(s, errors='replace'):
    print('Input:', repr(s))
    for enc in ['utf-8', 'utf-16', 'utf-32']:
        print(enc, ':', codecs.decode(s, enc, errors=errors))

s = b'\xff'
print('*** Error handler: replace')
test(s)
print('*** Error handler: add_one_codepoint (adding a as new first byte)')
test(s, errors='add_one_codepoint')
print('*** Error handler: add_utf16_bytes (adding ab as new first bytes)')
test(s, errors='add_utf16_bytes')
print('*** Error handler: add_utf32_bytes (adding abcd as new first bytes)')
test(s, errors='add_utf32_bytes')
