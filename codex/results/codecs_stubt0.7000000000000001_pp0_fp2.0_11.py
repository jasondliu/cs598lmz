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

str1 = 'A\u20ac\u20ac\u20ac'

for codec in ('utf-8', 'utf-16', 'utf-32'):
    print('-' * 30)
    print(codec)
    print('-' * 30)
    print(str1)
    print('-' * 30)

    encoded = str1.encode(codec)
    print(repr(encoded))
    print('-' * 30)

    decoded = encoded.decode(codec, 'replace')
    print(repr(decoded))
    print('-' * 30)

    decoded = encoded.decode(codec, 'ignore')
    print(repr(decoded))
    print('-' * 30)

    decoded = encoded.decode(codec, 'xmlcharrefreplace')
    print(repr(decoded))
    print('-' * 30)

    decoded = encoded.decode(codec, 'add_one_codepoint')
    print(repr(decoded))
    print('-' * 30)
