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

def test_UTF8_surrogates():
    s = b'\xed\xa0\x80' + b'\xed\xaf\xbf' + b'\xed\xb0\x80' + b'\xed\xbf\xbf'
    enc = 'utf-8'
    dec = 'utf-16-le'
    utf8_decoder = codecs.getincrementaldecoder(enc)()
    utf16_encoder = codecs.getincrementalencoder(dec)()

    expected = [
        (b'\x00\xd8', 2),
        (b'\x00\xdc', 2),
        (b'\x00\x01', 2),
        (b'\x00\x02', 2),
    ]

    for c in s:
        # The first time, this should raise a UTF-8 decoding error
        if utf8_decoder.buffer == b'':
            with self.assertRaises(UnicodeDecodeError) as cm:
                utf
