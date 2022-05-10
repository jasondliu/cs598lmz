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
    tests = [
        # one character missing
        (codecs.charmap_encode, 'abcde', '\u0f71\u0f72\u0f73\u0f74\u0f75\u0f76', 'add_one_codepoint', 'abcde'),
        (codecs.charmap_encode, 'abcde', '\u0f71\u0f72\u0f73\u0f74\u0f75\u0f76', 'add_one_codepoint', 'abcde'),

        # one UTF-16 character missing
        (codecs.utf_16_encode, 'a', '\u0f71\u0f72\u0f73', 'add_utf16_bytes', 'a'),
        (codecs.utf_16_le_encode, 'a', '\u0f71\u0f72\u0f73', 'add_utf16_bytes', 'a'),
        (codecs.utf_16
