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

for codec in ['ascii', 'utf8', 'utf_16_le']:
    a = "hello"
    print(codec, a)
    a = a.encode(codec, 'add_one_codepoint')
    print('\t', a, a.decode(codec, 'ignore'))

for codec in ['utf16', 'utf_16_le', 'utf_16_be']:
    a = b'hello'
    print(codec, a)
    a = bytes(a).decode(codec, 'add_utf16_bytes')
    print('\t', a, a.encode(codec))

for codec in ['utf32', 'utf_32_le', 'utf_32_be']:
    a = b'hello'
    print(codec, a)
    a = bytes(a).decode(codec, 'add_utf32_bytes')
    print('\t', a, a.encode(codec))

class codec(codecs.Codec):
    def
