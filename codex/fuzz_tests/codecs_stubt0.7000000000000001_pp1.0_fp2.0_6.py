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

if __name__ == '__main__':
    utf8_encoded_string = b'\xed\xa0\x80'.decode('utf-8')
    utf16_encoded_string = b'\xff\xfe\x00\xd8\x00\xdc'.decode('utf-16-le')
    utf32_encoded_string = b'\xff\xfe\x00\x00\x00\xd8\x00\x00\x00\xdc'.decode('utf-32-le')

    print(utf8_encoded_string)
    print(utf16_encoded_string)
    print(utf32_encoded_string)

    print(utf8_encoded_string.encode('utf-8', 'add_one_codepoint'))
    print(utf16_encoded_string.encode('utf-16-le', 'add_utf16_bytes'))
    print(utf32_encoded_string.encode('utf-32-le', 'add_utf32
