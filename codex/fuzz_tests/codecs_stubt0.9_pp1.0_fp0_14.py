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

# 1-byte characters
s = b'\xFF\xFF\xFF\xFF\xFF\xFF'
s = s.decode("latin-1", "replace")
assert len(s) == 30

s = b'\xFF\xFF\xFF\xFF\xFF\xFF'
s = s.decode("latin-1", "ignore")
assert len(s) == 0

s = b'\xFF\xFF\xFF\xFF\xFF\xFF'
s = s.decode("latin-1", "backslashreplace")
assert len(s) == 6
assert s == r'\xff\xff\xff\xff\xff\xff'


s = b'\xFF\xFF\xFF\xFF\xFF\xFF'
s = s.decode("latin-1", "add_one_codepoint")
assert len(s) == 7
assert '\xFF' not in s
assert s[0] == 'a'

# 2-
