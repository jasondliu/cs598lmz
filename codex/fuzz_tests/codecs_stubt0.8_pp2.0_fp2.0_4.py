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

def retry_with_backup(exc):
    return ('a', exc.end+1)

codecs.register_error("retry_with_backup", retry_with_backup)

def update_positions(exc):
    return (str(exc.start) + 'x', exc.end + 1)

codecs.register_error("update_positions", update_positions)

def test_1(encoding, errorhandler):
    s = b'\x81\x00\x00\x00'.decode(encoding, errorhandler)
    eq_(s, 'a')

def test_2(encoding, errorhandler):
    s = "abcd\x00\x00\x00".encode(encoding, errorhandler)
    eq_(s, b'abcdab')

def test_3(encoding, errorhandler):
    s = b'\x81\x81\x00\x00'.decode(encoding, errorhandler)
    eq_(s, 'aa')

def
