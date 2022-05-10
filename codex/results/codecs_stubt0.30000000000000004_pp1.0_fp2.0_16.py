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

# Test unicode-escape
for encoding in ['unicode-escape', 'raw-unicode-escape']:
    for errors in ['strict', 'ignore', 'replace', 'add_one_codepoint']:
        print(encoding, errors)
        print(codecs.decode('\\u1234', encoding, errors))
        print(codecs.decode('\\u1234\\u1234', encoding, errors))
        print(codecs.decode('\\u1234\\u1234\\u1234', encoding, errors))
        print(codecs.decode('\\u1234\\u1234\\u1234\\u1234', encoding, errors))
        print(codecs.decode('\\u1234\\u1234\\u1234\\u1234\\u1234', encoding, errors))
        print(codecs.decode('\\u1234\\u1234\\u1234\\u1234\\u1234\\u1234', encoding, errors))
        print(codecs.decode('\\u12
