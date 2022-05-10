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

def test_main():
    # Test UTF-8 decoding with errors
    for encoding in ('utf-8', 'utf_8'):
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint'):
            s = '\x80'
            if errors == 'replace':
                assert codecs.decode(s, encoding, errors) == '\ufffd'
            elif errors == 'ignore':
                assert codecs.decode(s, encoding, errors) == ''
            elif errors == 'add_one_codepoint':
                assert codecs.decode(s, encoding, errors) == 'a'
            else:
                raises(UnicodeDecodeError, codecs.decode, s, encoding, errors)

    # Test UTF-16 decoding with errors
    for encoding in ('utf-16', 'utf_16'):
        for errors in ('strict', 'replace', 'ignore', 'add_utf16_bytes'):
            s = b'\x80\x00'
            if errors == 'replace':

