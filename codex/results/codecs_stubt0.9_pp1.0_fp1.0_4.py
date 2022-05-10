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

try:
    str(b"\x00\xff\x00\xff\x00\xff", 'utf-32-be', 'add_one_codepoint')
except UnicodeDecodeError as e:
    print(e.reason)
    print(e.start)
    print(e.end)
    print(e.object)

print(str(b"\x00\xff\x00\xff\x00\xff", 'utf-16', 'add_utf16_bytes'))

print(str(b"\x00\xff\x00\xff\x00\xff", 'utf-32', 'add_utf32_bytes'))


assert str(b"\x00\xff\x00\xff\x00\xff", 'utf-32-be', 'surrogateescape') == '\U0010ffff\U0010ffff\U0010ffff'
assert str(b"\x00\xff\x00\xff\x00\xff", 'utf-32-be', 'surrorgatepass') == '\udcff\udcff
