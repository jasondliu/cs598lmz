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

with open("surrogate_error_testing.txt", "wb") as f:
    f.write(codecs.encode(u'a\udc80', 'utf-16-be'))
    f.write(codecs.encode(chr(0x03000), 'utf-16-be'))
    f.write(codecs.encode(u'\udc80a', 'utf-32-be'))
    f.write(codecs.encode(u'\udc80\udc80a', 'utf-32-be'))
    f.write(codecs.encode(u'\udc80\U00030000a', 'utf-32-be'))
print("testcase", repr(open("surrogate_error_testing.txt", "rb").read().decode("utf-8", "surrogateescape")))
print("testcase", repr(open("surrogate_error_testing.txt", "rb").read().decode("utf-16", "surrogateescape")))
print
