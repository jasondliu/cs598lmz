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
for encoding in ('unicode-escape', 'raw-unicode-escape'):
    print("Testing", encoding)
    for i in range(0x10000):
        ch = chr(i)
        # Test decoding
        s = codecs.escape_decode(ch)[0]
        if encoding == 'raw-unicode-escape':
            assert s == ch.encode('raw-unicode-escape'), (i, s)
        else:
            assert s == ch.encode('unicode-escape'), (i, s)
        s = codecs.escape_decode(ch, encoding)[0]
        assert s == ch.encode(encoding), (i, s)
        s = codecs.escape_decode(ch, 'strict', encoding)[0]
        assert s == ch.encode(encoding), (i, s)
        # Test encoding
        s = codecs.escape_encode(ch)[0]
        if encoding == 'raw-unicode-escape':
            assert s == ch.encode('
