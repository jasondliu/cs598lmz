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

# Test for SF bug #1519218:
# "UTF-8 decoder should handle error handler that returns a tuple"

u = '\u0b80'
u8 = u.encode('utf-8')

u8_bad = u8[:-1] + b'\x80'

for encoding in ('utf-8', 'utf-16', 'utf-32'):
    for errors in ('replace', 'strict', 'ignore', 'add_one_codepoint',
                   'add_utf16_bytes' if encoding == 'utf-16' else None,
                   'add_utf32_bytes' if encoding == 'utf-32' else None):
        print(encoding, errors)
        if errors == 'strict':
            u = u8
            u8_bad = u8_bad[:-1] + b'\x80'
        else:
            u = u8.decode(encoding, errors=errors)
            u8_bad = u8_bad.decode(encoding, errors=errors)
        print(u,
