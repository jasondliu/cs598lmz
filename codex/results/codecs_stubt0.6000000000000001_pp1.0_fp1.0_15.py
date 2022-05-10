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
    with support.check_warnings(('', UnicodeWarning)):
        # test decoder error handler
        for name, decoder, errorhandler in [
            ('utf-8', 'utf_8', 'add_one_codepoint'),
            ('utf-16', 'utf_16_le', 'add_utf16_bytes'),
            ('utf-32', 'utf_32_le', 'add_utf32_bytes'),
            ]:
            try:
                codecs.getdecoder(name)
            except LookupError:
                if name == 'utf-16':
                    continue
                raise
            # test with errorhandler as string
            data = bytes(range(0x80, 0x100))
            assert bytes(codecs.decode(data, name, errorhandler)) == data
            # test with errorhandler as function
            data = bytes(range(0x80, 0x100))
            assert bytes(codecs.decode(data, name, lambda exc:
                ("a", exc.start))) == data
            # test
