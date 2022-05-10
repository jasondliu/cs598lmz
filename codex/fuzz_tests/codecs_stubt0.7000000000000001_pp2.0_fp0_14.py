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

data = "a\udc80b"

for encoding in ['utf-8', 'utf-16', 'utf-32']:
    print(encoding.upper(), ":", data)
    print("\t>>>", data.encode(encoding, 'add_one_codepoint'))
    print("\t>>>", data.encode(encoding, 'add_utf16_bytes'))
    print("\t>>>", data.encode(encoding, 'add_utf32_bytes'))
