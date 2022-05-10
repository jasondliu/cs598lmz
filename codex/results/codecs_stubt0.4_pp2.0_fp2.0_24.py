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
    # Test the UTF-8 codec
    for encoding in ('utf-8', 'utf8'):
        for input, output in (
            ('abc', 'abc'),
            ('a\x80c', 'a\x80c'),
            ('a\xc0c', 'a\xc0c'),
            ('a\xc0\x80c', 'a\x80\x80c'),
            ('a\xc1c', 'a\xc1c'),
            ('a\xe0c', 'a\xe0c'),
            ('a\xe0\x80c', 'a\xe0\x80c'),
            ('a\xe0\x80\x80c', 'a\x80\x80\x80c'),
            ('a\xe1c', 'a\xe1c'),
            ('a\xe1\x80c', 'a\xe1\x80c'),
            ('a\xe1\x80\x80c', 'a\xe1\x80\x80c'),
            ('a\x
