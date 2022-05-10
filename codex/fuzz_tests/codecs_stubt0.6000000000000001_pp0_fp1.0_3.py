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

# UTF-8
print("UTF-8:")
print(b'\xc4\x8d\xed\xa0\x80\xe1\x80\x80\xe3\xa0\x80\xed\xb0\x80'.decode("utf-8", "add_one_codepoint"))
print(b'\xc4\x8d\xed\xa0\x80\xe1\x80\x80\xe3\xa0\x80\xed\xb0\x80'.decode("utf-8", "add_utf16_bytes"))
print(b'\xc4\x8d\xed\xa0\x80\xe1\x80\x80\xe3\xa0\x80\xed\xb0\x80'.decode("utf-8", "add_utf32_bytes"))

# UTF-16
print("\nUTF-16:")
print(b'\x00\x8d\x00\xd8\x00\x00\x00\xdc\x
