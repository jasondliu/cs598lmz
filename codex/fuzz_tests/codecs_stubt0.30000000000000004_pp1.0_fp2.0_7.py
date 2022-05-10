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

# Test the 'add_one_codepoint' error handler
for encoding in ('utf-8', 'utf-16', 'utf-32'):
    print('Encoding:', encoding)
    try:
        u'\uDC80'.encode(encoding, 'add_one_codepoint')
    except UnicodeEncodeError as e:
        print('Error:', e)

# Test the 'add_utf16_bytes' error handler
for encoding in ('utf-16', 'utf-32'):
    print('Encoding:', encoding)
    try:
        u'\uDC80'.encode(encoding, 'add_utf16_bytes')
    except UnicodeEncodeError as e:
        print('Error:', e)

# Test the 'add_utf32_bytes' error handler
for encoding in ('utf-32',):
    print('Encoding:', encoding)
    try:
        u'\uDC80'.encode(encoding, 'add_utf32_bytes')
    except UnicodeEncodeError as e:
        print('
