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
    # test __all__
    for name in ('ignore', 'replace', 'xmlcharrefreplace',
                 'backslashreplace', 'namereplace',
                 'add_one_codepoint', 'add_utf16_bytes', 'add_utf32_bytes'):
        assert hasattr(codecs, name)
        assert name in codecs.__all__

    # test backslashreplace()
    for c in ('\x00', '\x01', '\x02', '\xff', '\u0100', '\U00010001'):
        assert codecs.backslashreplace_errors(c) == (
            (r'\x%02x' % (c.encode('latin1')[0],)).encode('ascii'), c.encode('ascii').index(c))

    # test xmlcharrefreplace()
    for c in ('\x00', '\x01', '\x02', '\xff', '\u0100', '\U00010001'):
        assert codecs.xmlchar
