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

def test_add_codepoint_utf16_bytes_to_utf8():
    utf8 = '\u1234'.encode('utf-8', 'add_one_codepoint')
    utf16 = b'\x34\x12\x00\x00'
    utf32 = b'\x34\x12\x00\x00\x00\x00\x00\x00'
    assert utf8 == utf16.decode('utf-16', 'add_utf16_bytes')
    assert utf8 == utf32.decode('utf-32', 'add_utf32_bytes')

def test_translate():
    def mytranslate(exc):
        if exc.object[exc.start] == '\u1234':
            return ("a", exc.start + 1)
        return ("", exc.start + 1)
    utf8 = '\u1234'.encode('utf-8', 'ignore')
    assert utf8 == '\u1234'.encode('utf-8',
