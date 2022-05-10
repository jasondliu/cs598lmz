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

def test_utf16_decode(encoding, endianness):
    name = encoding + '_' + endianness
    decoder = codecs.getdecoder(name)
    encoder = codecs.getencoder(name)
    bytes = b'ab'
    if endianness == 'le':
        bytes = bytes[::-1]
    encoded_bytes = encoder(u'ab')[0]
    assert encoded_bytes == bytes
    encoded_bytes = b'\xff\xfe' + bytes
    assert decoder(encoded_bytes, 'strict')[0] == u'ab'
    assert decoder(encoded_bytes, 'add_one_codepoint')[0] == u'aab'
    assert decoder(encoded_bytes, 'add_utf16_bytes')[0] == u'aab'
    assert decoder(encoded_bytes, 'add_utf32_bytes')[0] == u'aab'

def test_utf32_decode(encoding, endianness):
   
