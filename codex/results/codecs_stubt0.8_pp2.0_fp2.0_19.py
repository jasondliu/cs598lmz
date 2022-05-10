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

# ASCII codecs, errors="strict"
s = b'abc\xffdef'
print(s.decode("ascii"))

# ASCII codecs, errors="replace"
print(s.decode("ascii", "replace"))

# ASCII codecs, errors="ignore"
print(s.decode("ascii", "ignore"))

# ASCII codecs, errors="add_one_codepoint"
print(s.decode("ascii", "add_one_codepoint"))

# ASCII codecs, errors="backslashreplace"
# (this is python specific)
print(s.decode("ascii", "backslashreplace"))

# ASCII codecs, errors="xmlcharrefreplace"
# (this is python specific)
print(s.decode("ascii", "xmlcharrefreplace"))

# UTF-16 codecs, errors="strict"
s = b'ab\xff\xffcd'
print(s.decode("utf-16"))

# UTF-16 codecs, errors="replace"
