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

# Test bytearray
for encoding in ('utf-8', 'utf-16', 'utf-32'):
    for error_handler in ('add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
        for input in ('abc', b'abc', bytearray(b'abc')):
            try:
                codecs.decode(input, encoding, error_handler)
            except UnicodeDecodeError:
                pass
            else:
                print(encoding, error_handler, input)

# Test memoryview
for encoding in ('utf-8', 'utf-16', 'utf-32'):
    for error_handler in ('add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
        for input in (b'abc', bytearray(b'abc'), memoryview(b'abc')):
            try:
                codecs.decode(input, encoding, error_handler)
            except UnicodeDecodeError:
                pass
            else:
                print
