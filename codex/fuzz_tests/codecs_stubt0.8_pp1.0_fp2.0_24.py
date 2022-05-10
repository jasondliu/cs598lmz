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

u = chr(0xdc00)
b = u.encode("utf16", "surrogatepass")

assert len(b) == 2

for codec in ('utf-16', 'utf-16-be', 'utf-16-le', 'utf-32', 'utf-32-be', 'utf-32-le'):
    assert codec + ' codec should raise UnicodeDecodeError on truncated input'
    raises(UnicodeDecodeError, u.encode, codec)
    assert codec + ' codec with add_one_codepoint should decode truncated input'
    assert u.encode(codec, "add_one_codepoint") == b'a'

    assert codec + ' codec with "surrogatepass" should decode truncated input'
    assert u.encode(codec, "surrogatepass") == b
    assert codec + ' codec with "replace" should decode truncated input'
    assert u.encode(codec, "replace") == b'\x00?'
    assert codec + ' codec with "ignore" should decode trunc
