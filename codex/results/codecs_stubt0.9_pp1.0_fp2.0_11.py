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

print("UTF-8", b'\xF0\x9F\x98\x82'.decode("utf-8", "surrogatepass"))
print("UTF-8", b'\xF0\x9F\x98\x82'.decode("utf-8", "replace"))
print("UTF-8", b'\xF0\x9F\x98\x82'.decode("utf-8", "ignore"))
print("UTF-8", b'\xF0\x9F\x98\x82'.decode("utf-8", "strict"))
print("UTF-8", b'\xF0\x9F\x98\x82'.decode("utf-8", "backslashreplace"))
print("UTF-8", b'\xF0\x9F\x98\x82'.decode("utf-8", "add_one_codepoint"))
print("UTF-8", b'\xF0\x9F\x98\x82'.decode("utf-8", "add_utf16_
