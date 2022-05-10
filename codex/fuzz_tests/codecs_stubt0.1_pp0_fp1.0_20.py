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
    for encoding in ('utf-8', 'utf_8'):
        for errors in ('strict', 'replace', 'ignore', 'add_one_codepoint',
                       'surrogateescape', 'surrogatepass', 'xmlcharrefreplace'):
            for input in (b'\xff', b'\xfe', b'\xfd', b'\xfc', b'\xfb',
                          b'\xfa', b'\xf9', b'\xf8', b'\xf7', b'\xf6',
                          b'\xf5', b'\xf4', b'\xf3', b'\xf2', b'\xf1',
                          b'\xf0', b'\xef', b'\xee', b'\xed', b'\xec',
                          b'\xeb', b'\xea', b'\xe9', b'\xe8', b'\xe7',
                          b'\xe6', b'\xe
