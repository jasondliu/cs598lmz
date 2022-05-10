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

unicode_samples = [
    b'\xc3\x81\xc3\x82\xc3\x83',
    b'\xff\xfe\x01\x02\x03',
    b'\xff\xfe\x00\x01\x00\x02\x00\x03',
]

multibyte_samples = [
    b'\xc3\x81\xc3\x82\xc3\x83',
    b'\x01\x02\x03',
    b'\x00\x01\x00\x02\x00\x03'
]

multibyte_decoded = (b'\x61\xc3\x81\xc3\x82\xc3\x83').decode('utf-8')

def test_ascii():
    encoder = codecs.getincrementalencoder('ascii')()
    decoder = codecs.getincrementaldecoder('ascii')()

    bytes = b''
    for chars in
