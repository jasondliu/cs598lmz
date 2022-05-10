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
    # Test UTF-8
    for i in range(0xD800, 0xE000):
        try:
            codecs.utf_8_decode(chr(i).encode('utf-8'), 'strict')
        except UnicodeDecodeError as exc:
            assert exc.object == chr(i).encode('utf-8')
            assert exc.start == 0
            assert exc.end == 1
            assert exc.reason == 'utf-8'
            assert exc.encoding == 'utf-8'
            assert exc.args == (chr(i).encode('utf-8'), 0, 1, 'utf-8')
            assert str(exc) == "'utf-8' codec can't decode byte 0x%x in position 0: %s" % (i, exc.reason)
        else:
            raise AssertionError("UnicodeDecodeError not raised")

        try:
            codecs.utf_8_decode(chr(i).encode('utf-8'), 'replace')
        except Unicode
