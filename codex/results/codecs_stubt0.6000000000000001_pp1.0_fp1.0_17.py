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

def check(encoding):
    print(encoding, "->", encoding.upper())
    try:
        codecs.encode(b'\x80', encoding)
    except UnicodeEncodeError as e:
        res = codecs.encode(b'\x80', encoding, "replace")
        if res != b'\xef\xbf\xbd':
            print("replace: expected U+FFFD, got", res.decode(encoding))
        res = codecs.encode(b'\x80', encoding, "add_one_codepoint")
        if res != b'a':
            print("add_one_codepoint: expected 'a', got", res.decode(encoding))
        res = codecs.encode(b'\x80', encoding, "add_utf16_bytes")
        if res != b'ab':
            print("add_utf16_bytes: expected 'ab', got", res.decode(encoding))
        res = codecs.encode(b'\x80', encoding, "add_
